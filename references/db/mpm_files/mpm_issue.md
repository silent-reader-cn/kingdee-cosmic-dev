# 项目问题-mpm_issue

## 项目问题-多语言表 t_mpm_issue_l

- **表名称：** 项目问题-多语言表
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

## 项目问题-主表 t_mpm_issue

- **表名称：** 项目问题-主表
- **表名：** t_mpm_issue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faskdate | 问题提出日期 | timestamp | 0 |  |  | null | 问题提出日期 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fpriority | 优先级 | bpchar | 1 |  |  | ' ' | 优先级,枚举: 1 :特高 2 :高 3 :中 4 :低 |
| 5 | factualclosedate | 实际关闭日期 | timestamp | 0 |  |  | null | 实际关闭日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | frelprojectid | 关联项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 8 | fcreatorid | 问题提出人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fexpectedclosedate | 期望关闭日期 | timestamp | 0 |  |  | null | 期望关闭日期 |
| 10 | fissuetypeid | 问题类型 | int8 | 64 |  | √ | 0 | [问题类型 mpm_issuetype](../mpm_files/mpm_issuetype.md) |
| 11 | fdescription_tag | 描述_详情 | text | 0 |  |  | ' ' | 描述_详情 |
| 12 | fprojectno | 项目编码 | varchar | 80 |  |  | ' ' | 项目编码 |
| 13 | fanalysis_tag | 问题分析_详情 | text | 0 |  |  | ' ' | 问题分析_详情 |
| 14 | fbillno | 问题编码 | varchar | 80 |  |  | ' ' | 问题编码 |
| 15 | fname | 问题名称 | varchar | 255 |  |  | ' ' | 问题名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbillstatus | 问题状态 | bpchar | 1 |  |  | ' ' | 问题状态,枚举: A :待评估 B :分析中 C :处理中 D :已关闭 E :作废 |
| 18 | fmanagerid | 负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fdescription | 描述 | text | 0 |  |  | ' ' | 描述 |
| 22 | fsolution | 应对措施 | text | 0 |  |  | ' ' | 应对措施 |
| 23 | fsolution_tag | 应对措施_详情 | text | 0 |  |  | ' ' | 应对措施_详情 |
| 24 | fanalysis | 问题分析 | text | 0 |  |  | ' ' | 问题分析 |
| 25 | ftask | 关联任务 | int8 | 64 |  | √ | 0 | [项目任务F7 mpm_task_f7](../mpm_files/mpm_task_f7.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

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
