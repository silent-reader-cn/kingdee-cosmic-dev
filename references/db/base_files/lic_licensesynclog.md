# 许可同步日志-lic_licensesynclog

## 许可同步日志-主表 t_lic_licsynclog

- **表名称：** 许可同步日志-主表
- **表名：** t_lic_licsynclog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcompare | 差异对比 | varchar | 30 |  | √ | ' ' | 差异对比,枚举: 0 :不能对比 1 :差异对比 2 :差异报告 |
| 3 | fopname | 操作名称 | varchar | 255 |  | √ | ' ' | 操作名称 |
| 4 | foptime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 5 | fissuccess | 是否成功 | bpchar | 1 |  |  | '0' | 是否成功 |
| 6 | fopdescription | 操作描述 | varchar | 255 |  | √ | ' ' | 操作描述 |
| 7 | fuserid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lic_licsynclog |  | fid |
| 2 | ix_lic_licsynclog_userid |  | fuserid |
