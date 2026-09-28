# 项目风险f7-mpm_risk_f7

## 项目风险f7-主表 t_mpm_riskearlywarning

- **表名称：** 项目风险f7-主表
- **表名：** t_mpm_riskearlywarning

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fname | 风险名称 | varchar | 255 |  | √ | ' ' | 风险名称 |
| 4 | fprojectid | 关联项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 5 | fbillstatus | 风险状态 | bpchar | 1 |  | √ | ' ' | 风险状态,枚举: A :未指派 B :待接收 C :跟进中 D :关闭 |
| 6 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 7 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 8 | fpriority | 优先级 | bpchar | 1 |  | √ | ' ' | 优先级,枚举: 1 :特高 2 :高 3 :中 4 :低 |
| 9 | fclosedate | fclosedate | timestamp | 0 |  |  | null |  |
| 10 | fplanclosedate | 预期关闭日期 | timestamp | 0 |  |  | null | 预期关闭日期 |
| 11 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 12 | fprocessor | 当前负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 14 | fcloser | fcloser | int8 | 64 |  | √ | 0 |  |
| 15 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 16 | fprocessstrategy | fprocessstrategy | bpchar | 1 |  | √ | ' ' |  |
| 17 | fprocessresult | fprocessresult | bpchar | 1 |  | √ | ' ' |  |
| 18 | fbillstatusbak | fbillstatusbak | bpchar | 1 |  | √ | ' ' |  |
| 19 | frisktypeid | 风险类型 | int8 | 64 |  | √ | 0 | [风险类型 mpm_risktype](../mpm_files/mpm_risktype.md) |
| 20 | ftaskid | 关联任务 | int8 | 64 |  | √ | 0 | [项目任务F7 mpm_task_f7](../mpm_files/mpm_task_f7.md) |
| 21 | fbillno | 风险编码 | varchar | 50 |  | √ | ' ' | 风险编码 |
| 22 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_riskearlywarning |  | fbillstatus,fprojectid |
| 2 | pk_mpm_riskearlywarning |  | fid |

---

## 项目风险f7-多语言表 t_mpm_riskearlywarning_l

- **表名称：** 项目风险f7-多语言表
- **表名：** t_mpm_riskearlywarning_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 风险名称 | varchar | 255 |  | √ | ' ' | 风险名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_riskearlywarning_l |  | fpkid |
