# 项目成本费用预算单-xkpb_costbudget_f7

## 项目成本费用预算单-主表 t_xkpb_costbudget

- **表名称：** 项目成本费用预算单-主表
- **表名：** t_xkpb_costbudget

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisstage | 仅按阶段进行预算编制 | bpchar | 1 |  | √ | '0' | 仅按阶段进行预算编制 |
| 3 | forgid | 编制组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftotalamount | ftotalamount | numeric | 23 | 10 | √ | 0 |  |
| 5 | fmultiorg | 多组织 | bpchar | 1 |  | √ | '0' | 多组织 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fsheetid | 表页ID | varchar | 36 |  | √ | ' ' | 表页ID |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fcalendarid | 预算日历 | int8 | 64 |  | √ | 0 | [预算日历 xkbm_budgetcalendar](../xkbm_files/xkbm_budgetcalendar.md) |
| 11 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fdeptid | 编制部门 | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |
| 14 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 15 | fcurrentapprover | fcurrentapprover | varchar | 255 |  | √ | ' ' |  |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fsubelegranularity | 细粒度编制方案 | int8 | 64 |  | √ | 0 | [成本子要素细粒度编制方案 xkpb_subelegranularity](../xkpb_files/xkpb_subelegranularity.md) |
| 18 | fbudgetsampleid | 预算模板 | varchar | 36 |  | √ | ' ' | [预算模板 xkbm_reportsample](../xkbm_files/xkbm_reportsample.md) |
| 19 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 20 | fbwbcurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 21 | fcurexpexpend | 预计支出(本位币) | numeric | 23 | 10 | √ | 0 | 预计支出(本位币) |
| 22 | fratetypeid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 23 | fiscontainlower | 包含下级 | bpchar | 1 |  | √ | '0' | 包含下级 |
| 24 | fyear | 年度 | varchar | 30 |  | √ | ' ' | 年度,枚举: |
| 25 | fexcutestatus | 执行状态 | bpchar | 1 |  | √ | '0' | 执行状态,枚举: 0 :未执行 1 :执行 |
| 26 | fnumber | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 27 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 28 | frptschemeid | 预算样式方案 | int8 | 64 |  | √ | 0 | [预算模板样式方案 xkbm_rptscheme](../xkbm_files/xkbm_rptscheme.md) |
| 29 | fbilltype | 单据类型 | varchar | 10 |  | √ | '1' | 单据类型,枚举: 1 :项目成本费用预算 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkpb_costbudget |  | fnumber |
| 2 | pk_t_xkpb_costbudget |  | fid |

---

## 项目成本费用预算单-多语言表 t_xkpb_costbudget_l

- **表名称：** 项目成本费用预算单-多语言表
- **表名：** t_xkpb_costbudget_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 2000 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkpb_costbudget_l |  | fpkid |
| 2 | idx_xkpb_costbudget_l |  | fid,flocaleid |

---

## 项目成本费用预算额-子表 t_xkpb_dimensionvalue

- **表名称：** 项目成本费用预算额-子表
- **表名：** t_xkpb_dimensionvalue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 3 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 4 | fdeptid | 部门 | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |
| 5 | forgfield | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fdimensionfield1 | 预置维度主键1 | varchar | 36 |  | √ | ' ' | 预置维度主键1 |
| 7 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fdimensionfield6 | 预置维度主键6 | varchar | 36 |  | √ | ' ' | 预置维度主键6 |
| 10 | famount | 预算额 | numeric | 23 | 10 | √ | 0 | 预算额 |
| 11 | fdimensionfield3 | 预置维度主键3 | varchar | 36 |  | √ | ' ' | 预置维度主键3 |
| 12 | fdimensionfield2 | 预置维度主键2 | varchar | 36 |  | √ | ' ' | 预置维度主键2 |
| 13 | fdimensionfield5 | 预置维度主键5 | varchar | 36 |  | √ | ' ' | 预置维度主键5 |
| 14 | fstageid | 阶段 | int8 | 64 |  | √ | 0 | [项目阶段 bd_projectphase](../basedata_files/bd_projectphase.md) |
| 15 | fdimensionfield4 | 预置维度主键4 | varchar | 36 |  | √ | ' ' | 预置维度主键4 |
| 16 | fentryprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 17 | fcurrencyfield | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | ftaskid | 任务 | int8 | 64 |  | √ | 0 | [项目任务F7 mpm_task_f7](../mpm_files/mpm_task_f7.md) |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkpb_costbudgetentry |  | fid |
| 2 | pk_t_xkpb_dimensionvalue |  | fentryid |
