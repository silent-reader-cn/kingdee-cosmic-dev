# 开放平台示例单据-openapi_unittest

## 关联子实体-子表 entryentity_lk

- **表名称：** 关联子实体-子表
- **表名：** entryentity_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | forderedqty_old | 采购分录已订货数量_原始携带值 | numeric | 23 | 10 |  | null | 采购分录已订货数量_原始携带值 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 7 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 8 | forderedqty | 采购分录已订货数量_确认携带值 | numeric | 23 | 10 |  | null | 采购分录已订货数量_确认携带值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tryentity_lk_fk |  | fentryid |
| 2 | pk_tryentity_lk |  | fpkid |

---

## 单据体-子表 t_openapi_ut_entry

- **表名称：** 单据体-子表
- **表名：** t_openapi_ut_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frequiredate | 采购分录需求日期 | timestamp | 0 |  |  | null | 采购分录需求日期 |
| 3 | fmodel | 采购分录规格模型 | varchar | 50 |  | √ | ' ' | 采购分录规格模型 |
| 4 | fmateria | 采购分录物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | famount | 采购分录金额 | numeric | 23 | 10 | √ | 0 | 采购分录金额 |
| 7 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | forderedqty | 采购分录已订货数量 | numeric | 23 | 10 | √ | 0 | 采购分录已订货数量 |
| 9 | fprice | 采购分录建议采购单价 | numeric | 23 | 10 | √ | 0 | 采购分录建议采购单价 |
| 10 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 11 | fmaterialname1 | fmaterialname1 | varchar | 50 |  | √ | ' ' |  |
| 12 | fapplyqty | 采购分录申请数量 | numeric | 23 | 10 | √ | 0 | 采购分录申请数量 |
| 13 | fbillstatusfield | 采购分录单据状态 | varchar | 50 |  | √ | ' ' | 采购分录单据状态,枚举: A :未下达 B :下达 C :关闭 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | funit | 采购分录计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_openapi_ut_entry |  | fentryid |
| 2 | idx_openapi_ut_entry_fmateria |  | fmateria |

---

## 子单据体1-子表 t_openapi_ut_subentry1

- **表名称：** 子单据体1-子表
- **表名：** t_openapi_ut_subentry1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftextfield6 | 收购子分录文本 | varchar | 50 |  | √ | ' ' | 收购子分录文本 |
| 2 | fintegerfield2 | 收购子分录文本整数 | int8 | 64 |  | √ | 0 | 收购子分录文本整数 |
| 3 | fbigintfield2 | 收购子分录文本长整数 | int8 | 64 |  | √ | 0 | 收购子分录文本长整数 |
| 4 | ftimefield1 | 收购子分录文本时间 | int8 | 64 |  | √ | 0 | 收购子分录文本时间 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fmaterielfield2 | 收购子分录文本物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fbilltypefield | 收购子分录文本单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_openapi_ut_subentry1 |  | fdetailid |
| 2 | idx_oput_sub1_entryid |  | fentryid |

---

## 开放平台示例单据-反写记录表 t_scm_purreq_zy_wb

- **表名称：** 开放平台示例单据-反写记录表
- **表名：** t_scm_purreq_zy_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scm_purreq_zy_wb |  | fentryid |
| 2 | idx_scm_purreq_zy_wb_fk |  | fid |

---

## 单据体1-子表 t_openapi_ut_entry1

- **表名称：** 单据体1-子表
- **表名：** t_openapi_ut_entry1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftextfield5 | 收购分录文本 | varchar | 50 |  | √ | ' ' | 收购分录文本 |
| 3 | fbigintfield1 | 收购分录长整数 | int8 | 64 |  | √ | 0 | 收购分录长整数 |
| 4 | ftextareafield | 收购分录多行文本 | varchar | 255 |  | √ | ' ' | 收购分录多行文本 |
| 5 | ftimefield | 收购分录时间 | int8 | 64 |  | √ | 0 | 收购分录时间 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fintegerfield1 | 收购分录整数 | int8 | 64 |  | √ | 0 | 收购分录整数 |
| 8 | fcheckboxfield | 收购分录复选框 | bpchar | 1 |  | √ | ' ' | 收购分录复选框 |
| 9 | fcurrencyfield | 收购分录币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fdecimalfield1 | 收购分录小数 | numeric | 23 | 10 | √ | 0 | 收购分录小数 |
| 12 | fcombofield | 收购分录下拉列表 | varchar | 50 |  | √ | ' ' | 收购分录下拉列表,枚举: 1 :1 2 :2 3 :3 4 :4 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_openapi_ut_entry1 |  | fentryid |
| 2 | idx_openapi_ut_entry1_id |  | fid |

---

## 开放平台示例单据-关联追踪表 t_scm_purreq_zy_tc

- **表名称：** 开放平台示例单据-关联追踪表
- **表名：** t_scm_purreq_zy_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scm_purreq_zy_tc_tbill |  | ftbillid |
| 2 | pk_scm_purreq_zy_tc |  | fid |
| 3 | idx_scm_purreq_zy_tc_tid |  | ftid |

---

## 子单据体-子表 t_openapi_ut_subentry

- **表名称：** 子单据体-子表
- **表名：** t_openapi_ut_subentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftextfield2 | 采购子分录文本 | varchar | 50 |  | √ | ' ' | 采购子分录文本 |
| 2 | fintegerfield | 采购子分录整数 | int8 | 64 |  | √ | 0 | 采购子分录整数 |
| 3 | forgfield | 采购子分录组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fbigintfield | 采购子分录长整数 | int8 | 64 |  | √ | 0 | 采购子分录长整数 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fmaterielfield1 | 采购子分录物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 9 | fdecimalfield | 采购子分录小数 | numeric | 23 | 10 | √ | 0 | 采购子分录小数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_oput_sub_entryid |  | fentryid |
| 2 | pk_openapi_ut_subentry |  | fdetailid |

---

## 多选基础资料-多选基础资料表 t_openapi_ut_multiple

- **表名称：** 多选基础资料-多选基础资料表
- **表名：** t_openapi_ut_multiple

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 第三方应用维护 openapi_3rdapps |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_openapi_ut_multiple |  | fpkid |
| 2 | idx_op_ut_basedataid |  | fbasedataid |

---

## 开放平台示例单据-主表 t_openapi_unittest

- **表名称：** 开放平台示例单据-主表
- **表名：** t_openapi_unittest

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapplyorg | 申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmaterielfield | 物料1 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | forg | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fusage | 用途 | varchar | 100 |  | √ | ' ' | 用途 |
| 7 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fitemclasstypefield | 基础资料类型 | varchar | 50 |  | √ | ' ' | 基础资料类型,枚举: bos_user :人员 bd_currency :币别 |
| 10 | fflexfield | 弹性域 | int8 | 64 |  | √ | 0 | null 002 |
| 11 | fapplier | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fpicturefield | 图片字段 | varchar | 255 |  | √ | ' ' | 图片字段 |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已关闭 |
| 16 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 18 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 19 | fmulcombofield | 多选下拉列表 | varchar | 50 |  | √ | ' ' | 多选下拉列表,枚举: 1 :1 2 :2 3 :3 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fdatefield | 日期2 | timestamp | 0 |  |  | null | 日期2 |
| 22 | fstarttime | 时间范围.开始 | int4 | 32 |  | √ | '-1' | 时间范围.开始 |
| 23 | fitemclassfield | 多类别基础资料 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fbasedatafield | 基础资料 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 25 | fendtime | 时间范围.结束 | int4 | 32 |  | √ | '-1' | 时间范围.结束 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_openapi_unittest_billno |  | fbillno |
| 2 | pk_openapi_unittest |  | fid |
