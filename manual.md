### 깃헙 쉬운 매뉴얼
window, VSCode terminal 에 최적화된 설명입니다.  

**로컬에 환경 만들기**
1. 앞으로 쓸 새 폴더 생성하고 그 안으로 들어갑니다.
	* mkdir 폴더명 : 폴더 생성
	* cd 폴더명 : 해당 폴더로 들어감
2. 버전관리를 시작합니다.
	* git init

**리모트(깃헙)과 연결 및 클론하기**  
현재 우리 레포지토리 주소: https://github.com/dataitgirls4/team_5.git  
1. 우리 레포지토리와 로컬을 연결합니다.
	* git remote add origin https://github.com/dataitgirls4/team_5.git
2. 클론합니다. 이때 새폴더가 만들어지고 복사됩니다. 폴더명은 마음대로.
	* git clone https://github.com/dataitgirls4/team_5.git 폴더명
	* cd 폴더명 : 해당 폴더로 들어감
	* ls -al : 폴더 내의 모든 파일을 보여줌
	
**브랜치 생성하고 작업하기**
현재 복사한 폴더 안에는 깃헙 레포지토리
1. **중요** 브랜치를 생성합니다.
	* git branch dev/본인이름 : 브랜치 생성
	* git checkout dev/본인이름 : 해당 브랜치로 HEAD 이동
2. 작업을 합니다.

**커밋하고 리모트로 푸쉬하기**
1. 커밋을 합니다.
	* git add 작업파일명
	* git commit -m "#이슈번호 커밋메시지"
2. 푸쉬합니다.
	* git push

**Pull Request**
1. 깃헙에서 위에서 푸쉬된 브랜치로 들어갑니다.  
2. pull request 버튼을 누르고, 변경된 사항에 관해서 자세하게 써줍니다.  
3-1. 새로운 파일을 올리는 경우, 본인이 main과 merge합니다.  
  이때, 작업하는 사이에 누군가 변경한 사항이 없는지 꼭 확인합니다.  
3-2. 기본 파일을 수정한 경우, 본인 앞에서 작업한 사람 or 팀원 전체와 상의합니다.  

**끝 / 위의 방법을 반복하면 됩니다**
