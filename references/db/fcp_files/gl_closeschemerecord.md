# 期末方案执行记录-gl_closeschemerecord

## 期末方案执行记录-主表 t_gl_closeschemerecord

- **表名称：** 期末方案执行记录-主表
- **表名：** t_gl_closeschemerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计期间 |
| 3 | fcreatorid | 执行用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fexecuteresult | 执行状态 | bpchar | 1 |  | √ | '0' | 执行状态,枚举: 0 :默认 1 :成功 2 :失败 |
| 5 | fcreatetime | 执行开始日期 | timestamp | 0 |  |  | null | 执行开始日期 |
| 6 | fschemeid | 期末方案 | int8 | 64 |  | √ | 0 | 期末方案 |
| 7 | fseq | 执行序号 | int4 | 32 |  | √ | 0 | 执行序号 |
| 8 | fendtime | 执行结束日期 | timestamp | 0 |  |  | null | 执行结束日期 |
| 9 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | 账簿 |
| 10 | fcloseitem | 执行方案标识 | varchar | 30 |  | √ | ' ' | 执行方案标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_closeschemerecord_fsid |  | fschemeid |
| 2 | pk_gl_closeschemerecord |  | fid |
