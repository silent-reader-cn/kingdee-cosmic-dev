# 项目问题f7-mpm_issue_f7

## 项目问题f7-多语言表 t_mpm_issue_l

- **表名称：** 项目问题f7-多语言表
- **表名：** t_mpm_issue_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 问题名称 | varchar | 255 |  | √ | ' ' | 问题名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_issue_l |  | fpkid |
| 2 | idx_mpm_issue_l |  | fid,flocaleid |

---

## 项目问题f7-主表 t_mpm_issue

- **表名称：** 项目问题f7-主表
- **表名：** t_mpm_issue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 2 | faskdate | faskdate | timestamp | 0 |  |  | null |  |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fpriority | 优先级 | bpchar | 1 |  |  | ' ' | 优先级,枚举: 1 :特高 2 :高 3 :中 4 :低 |
| 5 | factualclosedate | factualclosedate | timestamp | 0 |  |  | null |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | frelprojectid | 关联项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 8 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 9 | fexpectedclosedate | 期待关闭日期 | timestamp | 0 |  |  | null | 期待关闭日期 |
| 10 | fissuetypeid | 问题类型 | int8 | 64 |  | √ | 0 | [问题类型 mpm_issuetype](../mpm_files/mpm_issuetype.md) |
| 11 | fdescription_tag | fdescription_tag | text | 0 |  |  | ' ' |  |
| 12 | fprojectno | fprojectno | varchar | 80 |  |  | ' ' |  |
| 13 | fanalysis_tag | fanalysis_tag | text | 0 |  |  | ' ' |  |
| 14 | fbillno | 问题编码 | varchar | 80 |  |  | ' ' | 问题编码 |
| 15 | fname | 问题名称 | varchar | 255 |  |  | ' ' | 问题名称 |
| 16 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 17 | fbillstatus | 问题状态 | bpchar | 1 |  |  | ' ' | 问题状态,枚举: A :待评估 B :分析中 C :处理中 D :已关闭 E :作废 |
| 18 | fmanagerid | 当前负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 20 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 21 | fdescription | fdescription | text | 0 |  |  | ' ' |  |
| 22 | fsolution | fsolution | text | 0 |  |  | ' ' |  |
| 23 | fsolution_tag | fsolution_tag | text | 0 |  |  | ' ' |  |
| 24 | fanalysis | fanalysis | text | 0 |  |  | ' ' |  |
| 25 | ftask | 关联任务 | int8 | 64 |  | √ | 0 | [项目任务F7 mpm_task_f7](../mpm_files/mpm_task_f7.md) |
| 26 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_issue_billno |  | fbillno |
| 2 | idx_mpm_issue_task |  | ftask |
| 3 | pk_t_mpm_issue |  | fid |
| 4 | idx_mpm_issue_project |  | frelprojectid |
