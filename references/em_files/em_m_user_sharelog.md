# 用户分享日志-em_m_user_sharelog

## 用户分享日志-主表 t_er_mobi_sharelog

- **表名称：** 用户分享日志-主表
- **表名：** t_er_mobi_sharelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fshareparamter_tag | 参数_详情 | text | 0 |  |  | null | 参数_详情 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 4 | fexpirationtime | 过期时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 过期时间 |
| 5 | fshareparamter | 参数 | varchar | 255 |  |  | null | 参数 |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_mobi_sharelog |  | fid |
| 2 | idx_er_mobi_sharelog |  | fuserid |
