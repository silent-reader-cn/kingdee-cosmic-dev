# 人员初始登陆-bos_user_isfirstlogin

## 人员初始登陆-主表 t_sec_firstlogin

- **表名称：** 人员初始登陆-主表
- **表名：** t_sec_firstlogin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisfirstlogin | 首次登陆 | bpchar | 1 |  | √ | '1' | 首次登陆 |
| 3 | fbizapplist | fbizapplist | bpchar | 1 |  | √ | ' ' |  |
| 4 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fpagelist | fpagelist | bpchar | 1 |  | √ | '1' |  |
| 6 | fappmainpage | 首次应用首页 | bpchar | 1 |  | √ | ' ' | 首次应用首页 |
| 7 | fmainpage | 首次门户首页 | bpchar | 1 |  | √ | '1' | 首次门户首页 |
| 8 | fdevportal | fdevportal | bpchar | 1 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sec_firstlogin_pkey |  | fid |
| 2 | idx_sec_firstlogin_userid |  | fuserid |
