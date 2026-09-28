# 签名日志-bd_signmessagelog

## 签名日志-主表 t_bd_signmessagelog

- **表名称：** 签名日志-主表
- **表名：** t_bd_signmessagelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsigntime | 签名时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 签名时间 |
| 3 | fsignerid | 签名人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fsigntext | 指纹 | text | 0 |  |  | null | 指纹 |
| 5 | fbillpkid | 单据Id | varchar | 50 |  | √ | ' ' | 单据Id |
| 6 | fcleartext | 明文 | text | 0 |  |  | null | 明文 |
| 7 | fformid | 单据标识 | varchar | 36 |  | √ | ' ' | 单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_signmessagelog_pkey |  | fid |
| 2 | idx_bd_signlog |  | fformid,fbillpkid |
