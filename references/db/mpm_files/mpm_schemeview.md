# 方案预览-mpm_schemeview

## 方案预览-主表 t_mpm_scheme

- **表名称：** 方案预览-主表
- **表名：** t_mpm_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :未启用 1 :启用 2 :禁用 |
| 4 | fprogramdesc | 方案描述 | varchar | 200 |  |  | ' ' | 方案描述 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | foutputmodel | 分步输出模型 | varchar | 80 |  | √ | ' ' | 分步输出模型,枚举: |
| 7 | fprogramname | 方案名称 | varchar | 80 |  |  | ' ' | 方案名称 |
| 8 | ffirstmodelparam | 首选模型参数id | int8 | 64 |  | √ | 0 | 首选模型参数id |
| 9 | fsparemodelparam | 备选模型参数id | int8 | 64 |  | √ | 0 | 备选模型参数id |
| 10 | fstepoutset | 启用分步输出 | bpchar | 1 |  | √ | '0' | 启用分步输出 |
| 11 | fpromptword | 方案 | varchar | 2000 |  |  | ' ' | 方案 |
| 12 | froledesc | 角色描述 | varchar | 2000 |  |  | ' ' | 角色描述 |
| 13 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 14 | fsparemodel | 备选模型 | varchar | 80 |  | √ | ' ' | 备选模型,枚举: |
| 15 | fstepparam | 分步输出模型参数id | int8 | 64 |  | √ | 0 | 分步输出模型参数id |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | frenewpromptword | 重新生成 | varchar | 2000 |  |  | ' ' | 重新生成 |
| 18 | fstepoutput |  | varchar | 2000 |  |  | ' ' |  |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | ffirstmodel | 首选模型 | varchar | 80 |  |  | ' ' | 首选模型,枚举: |
| 21 | fformlinkrule | 表单关联规则 | int8 | 64 |  | √ | 0 | [表单关联规则单据头F7 formlinkrule_headerf7](../mpm_files/formlinkrule_headerf7.md) |
| 22 | fbillno | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_scheme |  | fid |
| 2 | idx_scheme_billno |  | fbillno |
