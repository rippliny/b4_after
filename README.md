# 프로젝트 개요

## 프로젝트
- B4 After Photos(Google Photo Clonecoding)
- Created by SpartaCodingClub NB Camp AI트랙 B4After Team

## 목표

- python package 중 Tensorflow 또는 Pytorch를 사용하여 이미지를 분류하는 웹서비스 구현
- 인식하려는 객체와 제공 서비스 목적에 따라 전이학습, 튜닝해서 모델을 학습

## 팀원 주요 역할

- Back-end :
    - django 프레임워크 : 고은혜, 정형빈
    - 사물인식 : 최동근
    - 이미지 메타데이터 추출 : 김명지
    - 속성별 분류 : 전다솔
- 팀원 모두 한 개 이상의 Back-End 기능 구현

# 주요 구현 기능

## Wireframe
![B4_After PNG](https://user-images.githubusercontent.com/112548916/196324020-cde51b40-9a9d-4c78-89c3-ab4d670789d1.png)

## 로그인

- DB에 저장된 username과 password를 비교하여 일치하지 않으면 오류 알림
- 만약 username이나 password가 빈칸으로 작성되었다면 오류 알림
- 로그인 완료 시 메인 페이지로 이동

## 회원 가입

- 로그인이 되어있지 않을 때만 회원 가입 페이지로 이동 가능
- 비밀번호와 비밀번호 확인이 일치하지 않으면 오류 알림
- 중복된 username 존재 시 오류 알림
- 회원 가입 완료 시 로그인 페이지로 이동

## 이미지 업로드

- DB에 이미지 파일 업로드

## 이미지 카테고리별 분류(메인페이지)

- 인물/사물 구분(Tensorflow 또는 pyTorch)
- 사물은 물체별로 구분
- 인물은 얼굴 인식을 통해 인물별 세부 구분(추가 선택사항)

## 이미지 상세히 보기

- 이미지(왼쪽)와 사진 정보를 보여줌

## 이미지 상세 정보 열람

- 사진 메타데이터를 표
    - 촬영 일자
    - 카메라 종류
    - 파일 이름
    - 업로드 방식
    - 저장상태
    - 촬영 장소

## 이미지 즐겨찾기 기능

- 이미지 상세 페이지에서 즐겨찾기(favorite와 유사) 클릭한 이미지만 보여주기

## 이미지 삭제 기능(휴지통으로 이동)

- 이미지 상세 페이지 또는 메인 페이지에서 삭제를 선택한 이미지를 휴지통으로 이동
- 휴지통 페이지에서 다시 한 번 이미지 삭제를 선택하면 데이터베이스에서 영구 삭제
- 복원을 선택하면 원래 페이지로 이미지 상태 되돌리기

## 더 자세한 내용
- https://www.notion.so/polarbear08/Machine-Learing-B4-After-Photos-b872ee7b91404087b2738592d64aa2fe
