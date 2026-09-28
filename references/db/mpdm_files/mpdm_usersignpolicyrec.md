# 用户签署应用隐私协议记录表-mpdm_usersignpolicyrec

## 用户签署应用隐私协议记录表-主表 t_mpdm_usersignpolrec

- **表名称：** 用户签署应用隐私协议记录表-主表
- **表名：** t_mpdm_usersignpolrec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frelhpschemeid | 关联首页方案 | int8 | 64 |  | √ | 0 | [移动首页方案 mpdm_hpschemeconfig](../mpdm_files/mpdm_hpschemeconfig.md) |
| 3 | fuseragent | 用户签署的客户端 | varchar | 512 |  | √ | ' ' | 用户签署的客户端 |
| 4 | fsigndate | 签署时间 | timestamp | 0 |  |  | null | 签署时间 |
| 5 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fschpolicyid | 应用隐私政策 | int8 | 64 |  | √ | 0 | [应用隐私政策 mpdm_schemepolicy](../mpdm_files/mpdm_schemepolicy.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_usersignpolrec |  | fid |
| 2 | idx_mpdm_usersignpolrec_user |  | fuserid |
