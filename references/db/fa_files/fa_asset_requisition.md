# 资产领用单-fa_asset_requisition

## 真单据体-子表 t_fa_asset_req_e

- **表名称：** 真单据体-子表
- **表名：** t_fa_asset_req_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freqstoreplace | 领用存放地点 | int8 | 64 |  | √ | 0 | 存放地点 fa_storeplace |
| 3 | fstoreplace | 存放地点 | int8 | 64 |  | √ | 0 | 存放地点 fa_storeplace |
| 4 | frequsestatus | 领用使用状态 | int8 | 64 |  | √ | 0 | 使用状态 fa_usestatus |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | frealcardid | 资产名称 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 8 | fusestate | 使用状态 | int8 | 64 |  | √ | 0 | 使用状态 fa_usestatus |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_asset_req_e_pkey |  | fentryid |
| 2 | idx_fa_are_fid |  | fid |

---

## 资产领用单-主表 t_fa_asset_requisition

- **表名称：** 资产领用单-主表
- **表名：** t_fa_asset_requisition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 1000 |  |  | ' ' | 备注 |
| 3 | fphone | fphone | varchar | 30 |  | √ | ' ' |  |
| 4 | fassetapplyid | 资产申请单id | int8 | 64 |  | √ | 0 | 资产申请单id |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :废弃 |
| 7 | fassetorgid | 资产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 领用人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fsigndate | 签收日期 | timestamp | 0 |  |  | null | 签收日期 |
| 11 | fhasvoucher | 凭证 | bpchar | 1 |  | √ | '0' | 凭证 |
| 12 | foperatedate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 13 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 14 | fsignuser | 签收人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fapplyreason | 申请事由 | varchar | 1000 |  |  | ' ' | 申请事由 |
| 18 | fdepartment | 领用人部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fsourcetype | 来源方式 | varchar | 30 |  | √ | ' ' | 来源方式,枚举: 1 :移动端移交或领用 2 :手工新增 |
| 20 | frequisitionuser | 领用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_assreq_fbillno |  | fbillno |
| 2 | t_fa_asset_requisition_pkey |  | fid |

---

## 关联子实体-子表 t_fa_asset_requisition_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fa_asset_requisition_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_asset_requisition_lk_pkey |  | fpkid |

---

## 资产领用单-关联追踪表 t_fa_asset_requisition_tc

- **表名称：** 资产领用单-关联追踪表
- **表名：** t_fa_asset_requisition_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_asset_requisition_tc_tbill |  | ftbillid |
| 2 | t_fa_asset_requisition_tc_pkey |  | fid |
| 3 | idx_fa_asset_requisition_tc_tid |  | ftid |

---

## 资产领用单-反写记录表 t_fa_asset_requisition_wb

- **表名称：** 资产领用单-反写记录表
- **表名：** t_fa_asset_requisition_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_asset_requisition_wb_pkey |  | fentryid |
