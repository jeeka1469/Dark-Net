// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract Verifier {
    mapping(uint => bool) public verifiedSolutions;

    event SolutionVerified(uint indexed submissionId, bool verified);

    function verify(uint submissionId, bool status) public {
        verifiedSolutions[submissionId] = status;
        emit SolutionVerified(submissionId, status);
    }
}