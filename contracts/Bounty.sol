// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract Bounty {
    struct Submission {
        address submitter;
        string solution;
        bool verified;
    }

    mapping(uint => Submission) public submissions;
    uint public submissionCount;

    event SolutionSubmitted(uint indexed submissionId, address indexed submitter, string solution);
    event SolutionVerified(uint indexed submissionId, bool verified);

    function submitSolution(string memory _solution) public {
        submissions[submissionCount] = Submission(msg.sender, _solution, false);
        emit SolutionSubmitted(submissionCount, msg.sender, _solution);
        submissionCount++;
    }

    function verifySolution(uint _submissionId, bool _status) public {
        submissions[_submissionId].verified = _status;
        emit SolutionVerified(_submissionId, _status);
    }
}