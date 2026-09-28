# 销售补充协议-conm_salsupagrt

## 销售补充协议-主表 t_conm_salsupagrt

- **表名称：** 销售补充协议-主表
- **表名：** t_conm_salsupagrt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fcancelstatus | 作废状态 | varchar | 5 |  | √ | ' ' | 作废状态,枚举: A :未作废 B :已作废 |
| 4 | fsigndate | 签章日期 | timestamp | 0 |  |  | null | 签章日期 |
| 5 | fparty2nd | 乙方 | varchar | 255 |  | √ | ' ' | 乙方 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | freviewstatus | 评审状态 | varchar | 5 |  | √ | ' ' | 评审状态,枚举: A :未评审 B :评审中 C :通过 D :不通过 E :未启用 |
| 8 | fdetail | 详情信息 | varchar | 512 |  |  | null | 详情信息 |
| 9 | femail2nd | 乙方邮箱 | varchar | 100 |  | √ | ' ' | 乙方邮箱 |
| 10 | fcategoryid | 合同种类 | int8 | 64 |  | √ | 0 | [合同种类 conm_category](../conm_files/conm_category.md) |
| 11 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 12 | fbillno | 协议编号 | varchar | 80 |  | √ | ' ' | 协议编号 |
| 13 | fdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | ftemplateid | 合同模板 | int8 | 64 |  | √ | 0 | [合同模板 conm_template](../conm_files/conm_template.md) |
| 15 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fsrcbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | fbiztimeend | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 19 | fbillname | 协议名称 | varchar | 100 |  | √ | ' ' | 协议名称 |
| 20 | ftypeid | 合同类型 | int8 | 64 |  | √ | 0 | [合同类型 conm_type](../conm_files/conm_type.md) |
| 21 | fpartcid | 第三方 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 22 | fparty1st | 甲方 | varchar | 255 |  | √ | ' ' | 甲方 |
| 23 | fvalidstatus | 生效状态 | varchar | 5 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 C :已失效 |
| 24 | fcanceldate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 25 | ffilingdate | 归档日期 | timestamp | 0 |  |  | null | 归档日期 |
| 26 | femail1st | 甲方邮箱 | varchar | 100 |  | √ | ' ' | 甲方邮箱 |
| 27 | fsrccontractnum | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 30 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 31 | fvaliderid | 生效人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fiselecsignature | 是否电子签章 | bpchar | 1 |  | √ | '0' | 是否电子签章 |
| 33 | foperatorid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 34 | fsrcversion | 合同版本号 | varchar | 30 |  | √ | ' ' | 合同版本号 |
| 35 | fcontpartiesid | 合同主体 | int8 | 64 |  | √ | 0 | [合同主体 conm_contparties](../conm_files/conm_contparties.md) |
| 36 | fdetail_tag | 详情信息_详情 | text | 0 |  |  | null | 详情信息_详情 |
| 37 | freviewdate | 评审日期 | timestamp | 0 |  |  | null | 评审日期 |
| 38 | fbiztime | 签订日期 | timestamp | 0 |  |  | null | 签订日期 |
| 39 | fsrccontractname | 合同名称 | varchar | 100 |  | √ | ' ' | 合同名称 |
| 40 | fdocumentid | 电签合同ID | varchar | 50 |  | √ | ' ' | 电签合同ID |
| 41 | fcancelerid | 作废人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | ffilingstatus | 归档状态 | varchar | 5 |  | √ | ' ' | 归档状态,枚举: A :未归档 B :已归档 C :未启用 |
| 44 | ffilingerid | 归档人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fphone2nd | 乙方电话 | varchar | 255 |  | √ | ' ' | 乙方电话 |
| 46 | fsignstatus | 签章状态 | varchar | 5 |  | √ | ' ' | 签章状态,枚举: A :未签章 B :签章完成 C :未启用 D :乙方已签 E :甲方已签 F :上传完成 |
| 47 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 48 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 49 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 50 | fcontactperson1st | 甲方联系人 | varchar | 60 |  | √ | ' ' | 甲方联系人 |
| 51 | foperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 52 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 53 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 54 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 55 | fsignerid | 签章人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 56 | ftemplateentryid | 模板版本 | int8 | 64 |  | √ | 0 | [模板版本 conm_tempfileentry](../conm_files/conm_tempfileentry.md) |
| 57 | fbiztimebegin | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |
| 58 | fphone1st | 甲方电话 | varchar | 255 |  | √ | ' ' | 甲方电话 |
| 59 | fcontactperson2nd | 乙方联系人 | varchar | 60 |  | √ | ' ' | 乙方联系人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_salsupagrt_org |  | forgid,fbiztime,fid |
| 2 | t_conm_salsupagrt_pkey |  | fid |
| 3 | idx_conm_salsupagrt_billno |  | fbillno |

---

## 销售补充协议-反写记录表 t_conm_salsupagrt_wb

- **表名称：** 销售补充协议-反写记录表
- **表名：** t_conm_salsupagrt_wb

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
| 1 | idx_conm_salsupagrt_wb_fk |  | fid |
| 2 | t_conm_salsupagrt_wb_pkey |  | fentryid |

---

## 关联子实体-子表 t_conm_salsupagrt_lk

- **表名称：** 关联子实体-子表
- **表名：** t_conm_salsupagrt_lk

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
| 1 | t_conm_salsupagrt_lk_pkey |  | fpkid |
| 2 | idx_conm_salsupagrt_lk_fk |  | fid |

---

## 销售补充协议-关联追踪表 t_conm_salsupagrt_tc

- **表名称：** 销售补充协议-关联追踪表
- **表名：** t_conm_salsupagrt_tc

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
| 1 | t_conm_salsupagrt_tc_pkey |  | fid |
| 2 | idx_conm_salsupagrt_tc_tid |  | ftid |
| 3 | idx_conm_salsupagrt_tc_tbill |  | ftbillid |
