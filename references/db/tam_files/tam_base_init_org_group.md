# 汇总方案初始化-tam_base_init_org_group

## 汇总方案初始化-主表 t_tam_base_init_org_group

- **表名称：** 汇总方案初始化-主表
- **表名：** t_tam_base_init_org_group

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 完成状态 | varchar | 50 |  | √ | ' ' | 完成状态,枚举: 0 :未完成 1 :已完成 |
| 3 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | fbasedataname | 资料名称 | varchar | 50 |  | √ | ' ' | 资料名称,枚举: qysds :企业所得税汇总方案 zzs :增值税汇总方案 sljsjj :地方水利建设基金汇总方案 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fsummarytype | 汇总类型 | varchar | 50 |  | √ | ' ' | 汇总类型,枚举: 0 :独立申报 1 :汇总申报 |
| 7 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fglhzfa | 关联汇总方案 | varchar | 200 |  | √ | ' ' | 关联汇总方案 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tam_base_init_org_group |  | fid |
| 2 | idx_tam_base_init_org_group_1 |  | forgid |
