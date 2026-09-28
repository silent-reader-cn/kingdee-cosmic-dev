# 采购补充协议-conm_pursupagrt

## 关联子实体-子表 t_conm_pursupagrt_lk

- **表名称：** 关联子实体-子表
- **表名：** t_conm_pursupagrt_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_pursupagrt_lk_pkey |  | fpkid |
| 2 | idx_conm_pursupagrt_lk_fk |  | fid |

---

## 采购补充协议-主表 t_conm_pursupagrt

- **表名称：** 采购补充协议-主表
- **表名：** t_conm_pursupagrt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fcancelstatus | 作废状态 | varchar | 5 |  | √ | ' ' | 作废状态,枚举: A :未作废 B :已作废 |
| 4 | fsigndate | 签章日期 | timestamp | 0 |  |  | null | 签章日期 |
| 5 | fparty2nd | 乙方 | varchar | 255 |  | √ | ' ' | 乙方 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | freviewstatus | 评审状态 | varchar | 5 |  | √ | ' ' | 评审状态,枚举: A :未评审 B :评审中 C :通过 D :不通过 E :未启用 |
| 8 | fdetail | 详情信息 | varchar | 512 |  |  | null | 详情信息 |
| 9 | fcategoryid | 合同种类 | int8 | 64 |  | √ | 0 | 合同种类 conm_category |
| 10 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 11 | fbillno | 协议编号 | varchar | 80 |  | √ | ' ' | 协议编号 |
| 12 | fdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | ftemplateid | 合同模板 | int8 | 64 |  | √ | 0 | 合同模板 conm_template |
| 14 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fsrcbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 16 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 17 | fbiztimeend | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 18 | fbillname | 协议名称 | varchar | 100 |  | √ | ' ' | 协议名称 |
| 19 | fsupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 20 | ftypeid | 合同类型 | int8 | 64 |  | √ | 0 | 合同类型 conm_type |
| 21 | fpartcid | 第三方 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 22 | fparty1st | 甲方 | varchar | 255 |  | √ | ' ' | 甲方 |
| 23 | fvalidstatus | 生效状态 | varchar | 5 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 C :已失效 |
| 24 | fcanceldate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 25 | ffilingdate | 归档日期 | timestamp | 0 |  |  | null | 归档日期 |
| 26 | fsrccontractnum | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 29 | fvaliderid | 生效人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fiselecsignature | 是否电子签章 | bpchar | 1 |  | √ | '0' | 是否电子签章 |
| 31 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 32 | fsrcversion | 合同版本号 | varchar | 30 |  | √ | ' ' | 合同版本号 |
| 33 | fcontpartiesid | 合同主体 | int8 | 64 |  | √ | 0 | 合同主体 conm_contparties |
| 34 | fdetail_tag | 详情信息_详情 | text | 0 |  |  | null | 详情信息_详情 |
| 35 | freviewdate | 评审日期 | timestamp | 0 |  |  | null | 评审日期 |
| 36 | fbiztime | 签订日期 | timestamp | 0 |  |  | null | 签订日期 |
| 37 | fsrccontractname | 合同名称 | varchar | 100 |  | √ | ' ' | 合同名称 |
| 38 | fdocumentid | 电签合同ID | varchar | 50 |  | √ | ' ' | 电签合同ID |
| 39 | fcancelerid | 作废人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | ffilingstatus | 归档状态 | varchar | 5 |  | √ | ' ' | 归档状态,枚举: A :未归档 B :已归档 C :未启用 |
| 42 | ffilingerid | 归档人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 43 | fphone2nd | 乙方电话 | varchar | 255 |  | √ | ' ' | 乙方电话 |
| 44 | fsignstatus | 签章状态 | varchar | 5 |  | √ | ' ' | 签章状态,枚举: A :未签章 B :签章完成 C :未启用 D :乙方已签 E :甲方已签 F :上传完成 |
| 45 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 46 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 47 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 48 | fcontactperson1st | 甲方联系人 | varchar | 60 |  | √ | ' ' | 甲方联系人 |
| 49 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 50 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 51 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 52 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 53 | fsignerid | 签章人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 54 | ftemplateentryid | 模板版本 | int8 | 64 |  | √ | 0 | 模板版本 conm_tempfileentry |
| 55 | fbiztimebegin | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |
| 56 | fphone1st | 甲方电话 | varchar | 255 |  | √ | ' ' | 甲方电话 |
| 57 | fcontactperson2nd | 乙方联系人 | varchar | 60 |  | √ | ' ' | 乙方联系人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_pursupagrt_pkey |  | fid |
| 2 | idx_conm_pursupagrt_billno |  | fbillno |
| 3 | idx_conm_pursupagrt_org |  | forgid,fbiztime,fid |

---

## 采购补充协议-反写记录表 t_conm_pursupagrt_wb

- **表名称：** 采购补充协议-反写记录表
- **表名：** t_conm_pursupagrt_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_pursupagrt_wb_fk |  | fid |
| 2 | t_conm_pursupagrt_wb_pkey |  | fentryid |

---

## 采购补充协议-关联追踪表 t_conm_pursupagrt_tc

- **表名称：** 采购补充协议-关联追踪表
- **表名：** t_conm_pursupagrt_tc

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
| 1 | idx_conm_pursupagrt_tc_tid |  | ftid |
| 2 | t_conm_pursupagrt_tc_pkey |  | fid |
| 3 | idx_conm_pursupagrt_tc_tbill |  | ftbillid |
