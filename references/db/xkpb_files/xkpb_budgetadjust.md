# 项目预算变更单-xkpb_budgetadjust

## 项目预算变更单-多语言表 t_xkpb_budgetadjust_l

- **表名称：** 项目预算变更单-多语言表
- **表名：** t_xkpb_budgetadjust_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fadjustreason | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_xkpb_budgetadjust_l |  | fid,flocaleid |
| 2 | pk_xkpb_budgetadjust_l |  | fpkid |

---

## 预算变更-子表 t_xkpb_budgetadjustentry

- **表名称：** 预算变更-子表
- **表名：** t_xkpb_budgetadjustentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryorg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fdeptid | 部门 | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |
| 4 | fcheckamount | 核定调整额 | numeric | 23 | 10 | √ | 0 | 核定调整额 |
| 5 | fdimensionfield1 | 预置维度主键1 | varchar | 36 |  | √ | ' ' | 预置维度主键1 |
| 6 | fentryproject | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 7 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fdimensionfield6 | 预置维度主键6 | varchar | 36 |  | √ | ' ' | 预置维度主键6 |
| 10 | fapplyamount | 申请调整额 | numeric | 23 | 10 | √ | 0 | 申请调整额 |
| 11 | fdimensionfield3 | 预置维度主键3 | varchar | 36 |  | √ | ' ' | 预置维度主键3 |
| 12 | fdimensionfield2 | 预置维度主键2 | varchar | 36 |  | √ | ' ' | 预置维度主键2 |
| 13 | fdimensionfield5 | 预置维度主键5 | varchar | 36 |  | √ | ' ' | 预置维度主键5 |
| 14 | fstageid | 阶段 | int8 | 64 |  | √ | 0 | [项目阶段 bd_projectphase](../basedata_files/bd_projectphase.md) |
| 15 | fdimensionfield4 | 预置维度主键4 | varchar | 36 |  | √ | ' ' | 预置维度主键4 |
| 16 | ffinalamount | 调整后 | numeric | 23 | 10 | √ | 0 | 调整后 |
| 17 | ftask | 任务 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 18 | fsubelement | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 19 | fstartamount | 调整前 | numeric | 23 | 10 | √ | 0 | 调整前 |
| 20 | fdatasource | 数据来源 | varchar | 10 |  | √ | '1' | 数据来源,枚举: 0 :历史数据 1 :本单新增 |
| 21 | fentryremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkpb_budgetadjustentry |  | fentryid |
| 2 | idx_xkpb_budgetadjustentry |  | fid |

---

## 预算变更-多语言表 t_xkpb_budgetadjustentry_l

- **表名称：** 预算变更-多语言表
- **表名：** t_xkpb_budgetadjustentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fentryremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkpb_budgetadjustentry_l |  | fpkid |
| 2 | idx_budgetadjustentry_l |  | fentryid,flocaleid |

---

## 项目预算变更单-主表 t_xkpb_budgetadjust

- **表名称：** 项目预算变更单-主表
- **表名：** t_xkpb_budgetadjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fislastversion | 是否为最新版本 | bpchar | 1 |  | √ | '0' | 是否为最新版本 |
| 4 | fcurrentapprover | 流程当前节点及处理人 | varchar | 255 |  | √ | ' ' | 流程当前节点及处理人 |
| 5 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 编制组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | ftotalamount | 单据体汇总数(隐藏) | numeric | 23 | 10 | √ | 0 | 单据体汇总数(隐藏) |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fadjustreason | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fiscontainlower | 包含下级 | bpchar | 1 |  | √ | '0' | 包含下级 |
| 14 | fyear | 年度 | varchar | 10 |  | √ | ' ' | 年度 |
| 15 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fcostbudget | 项目成本费用预算单 | int8 | 64 |  | √ | 0 | [项目成本费用预算单 xkpb_costbudget_f7](../xkpb_files/xkpb_costbudget_f7.md) |
| 18 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkpb_budgetadjust |  | fid |
| 2 | idx_xkpb_budgetadjust_cb |  | fcostbudget |
