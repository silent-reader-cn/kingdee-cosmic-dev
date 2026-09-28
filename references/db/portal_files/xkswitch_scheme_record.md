# 用户切换首页方案记录-xkswitch_scheme_record

## 用户切换首页方案记录-主表 t_xk_switch_record

- **表名称：** 用户切换首页方案记录-主表
- **表名：** t_xk_switch_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fswitchstatus | 切换状态 | varchar | 50 |  | √ | ' ' | 切换状态,枚举: 0 :不切换 1 :切换 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fuserid | 人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xk_switch_record |  | fid |
| 2 | idx_t_xk_switch_record_user |  | fuserid |
