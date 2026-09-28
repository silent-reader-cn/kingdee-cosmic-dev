# 评审申请单-conm_reviewapply

## 评审申请单-反写记录表 t_conm_reviewapply_wb

- **表名称：** 评审申请单-反写记录表
- **表名：** t_conm_reviewapply_wb

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
| 1 | idx_conm_reviewapply_wb_fk |  | fid |
| 2 | t_conm_reviewapply_wb_pkey |  | fentryid |

---

## 评审申请单-主表 t_conm_reviewapply

- **表名称：** 评审申请单-主表
- **表名：** t_conm_reviewapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fbiztime | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 4 | fparty2nd | 乙方 | varchar | 255 |  | √ | ' ' | 乙方 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 8 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 9 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fdeptid | 申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已通过 D :未通过 |
| 12 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 13 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fbizuserid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fcontractname | 合同名称 | varchar | 100 |  | √ | ' ' | 合同名称 |
| 17 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fbillname | 单据名称 | varchar | 100 |  | √ | ' ' | 单据名称 |
| 20 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 21 | ftypeid | 合同类型 | int8 | 64 |  | √ | 0 | 合同类型 conm_type |
| 22 | fpartcid | 第三方 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 23 | fparty1st | 甲方 | varchar | 255 |  | √ | ' ' | 甲方 |
| 24 | fcontractnum | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_reviewapply_billno |  | fbillno |
| 2 | idx_conm_reviewapply_org |  | forgid,fbiztime,fid |
| 3 | t_conm_reviewapply_pkey |  | fid |

---

## 评审申请单-关联追踪表 t_conm_reviewapply_tc

- **表名称：** 评审申请单-关联追踪表
- **表名：** t_conm_reviewapply_tc

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
| 1 | t_conm_reviewapply_tc_pkey |  | fid |
| 2 | idx_conm_reviewapply_tc_tid |  | ftid |
| 3 | idx_conm_reviewapply_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_conm_reviewapply_lk

- **表名称：** 关联子实体-子表
- **表名：** t_conm_reviewapply_lk

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
| 1 | t_conm_reviewapply_lk_pkey |  | fpkid |
| 2 | idx_conm_reviewapply_lk_fk |  | fid |
