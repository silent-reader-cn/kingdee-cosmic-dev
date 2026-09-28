# 资产申请单-fa_asset_apply_admin

## 资产明细-子表 t_fa_apply_asseet_detail

- **表名称：** 资产明细-子表
- **表名：** t_fa_apply_asseet_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fassetname | 资产名称 | varchar | 60 |  | √ | ' ' | 资产名称 |
| 4 | fstoreplace | fstoreplace | int8 | 64 |  | √ | 0 |  |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fnumber | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fusestate | fusestate | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_apply_asseet_detail_pkey |  | fentryid |
| 2 | idx_fa_aad_fid |  | fid |

---

## 资产申请单-主表 t_fa_asset_apply

- **表名称：** 资产申请单-主表
- **表名：** t_fa_asset_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisbuildshopapply | 生成采购申请 | varchar | 1 |  | √ | ' ' | 生成采购申请,枚举: A :是 B :否 |
| 3 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 6 | fisbuildapplybill | 生成领用单 | varchar | 1 |  | √ | ' ' | 生成领用单,枚举: A :是 B :否 |
| 7 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :废弃 |
| 8 | fassetorgid | 资产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | forgid | 申请人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fhasvoucher | 凭证 | bpchar | 1 |  | √ | '0' | 凭证 |
| 12 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 13 | fdeptmentid | 申请人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fstoreplace | 存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fapplyreason | 申请事由 | varchar | 1000 |  |  | ' ' | 申请事由 |
| 18 | fapplyusername | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fuserphone | fuserphone | varchar | 30 |  | √ | ' ' |  |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_asset_apply_pkey |  | fid |
| 2 | idx_fa_assapp_fbillno |  | fbillno |
