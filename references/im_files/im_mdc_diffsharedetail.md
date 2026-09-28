# 领料差异分摊明细-im_mdc_diffsharedetail

## 分摊明细-子表 t_im_mdc_shdifsharedetail

- **表名称：** 分摊明细-子表
- **表名：** t_im_mdc_shdifsharedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmadebasenum | 应发基本数量 | numeric | 23 | 10 | √ | 0 | 应发基本数量 |
| 3 | fassignnum | 已生成数量 | numeric | 23 | 10 | √ | 0 | 已生成数量 |
| 4 | fsharenum | 应分摊数量 | numeric | 23 | 10 | √ | 0 | 应分摊数量 |
| 5 | fshinvtype | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 6 | fshproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 7 | fshorderentryid | 生产工单行f7 | int8 | 64 |  | √ | 0 | 生产工单分录f7 im_mdc_mftorderf7 |
| 8 | fsharebasenum | 应分摊基本数量 | numeric | 23 | 10 | √ | 0 | 应分摊基本数量 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fshbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fassignstauts | 生成情况 | varchar | 50 |  | √ | ' ' | 生成情况,枚举: A :未生成 C :已生成 |
| 12 | fshauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 13 | fshinvstatus | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 14 | fdiffshareremark_tag | 分摊描述_详情 | text | 0 |  |  | null | 分摊描述_详情 |
| 15 | fshexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 16 | fshstockno | 组件编号 | varchar | 50 |  | √ | ' ' | 组件编号 |
| 17 | fpickbasenum | 已领基本数量 | numeric | 23 | 10 | √ | 0 | 已领基本数量 |
| 18 | fsharestatus | 分摊情况 | varchar | 50 |  | √ | ' ' | 分摊情况,枚举: A :未分摊 B :部分分摊 C :完全分摊 |
| 19 | fshisbackflush | 倒冲 | varchar | 50 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :始终倒冲 C :工作中心决定是否倒冲 |
| 20 | fshmaterial | 组件物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 21 | finvunit | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | ftransactiontypeid | ftransactiontypeid | int8 | 64 |  | √ | 0 |  |
| 23 | fshwarehouse | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 24 | fshownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 25 | fshkeepertype | 保管者类型 | varchar | 50 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 26 | fshkeeper | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fshdiffshareno | fshdiffshareno | varchar | 50 |  | √ | ' ' |  |
| 28 | fshowner | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fstockid | 组件id | int8 | 64 |  | √ | 0 | 组件id |
| 30 | factsharebasenum | 实际分摊基本数量 | numeric | 23 | 10 | √ | 0 | 实际分摊基本数量 |
| 31 | fstockentryid | 组件分录id | int8 | 64 |  | √ | 0 | 组件分录id |
| 32 | fassignremark | 生成描述 | varchar | 255 |  | √ | ' ' | 生成描述 |
| 33 | fshproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 34 | factsharenum | 实际分摊数量 | numeric | 23 | 10 | √ | 0 | 实际分摊数量 |
| 35 | fshqtytype | 用量类型 | varchar | 50 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :变动 |
| 36 | fshlotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 37 | fshmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 38 | fdiffshareremark | 分摊描述 | varchar | 255 |  | √ | ' ' | 分摊描述 |
| 39 | fassignremark_tag | 生成描述_详情 | text | 0 |  |  | null | 生成描述_详情 |
| 40 | fshorderno | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 41 | fshlocation2 | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 43 | fshdiffshareid | 倒冲差异分摊f7 | int8 | 64 |  | √ | 0 | 领料差异分摊F7 im_mdc_backdiffshare_f7 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_shdifsharedetail |  | fentryid |
| 2 | idx_t_im_mdc_sharedetail |  | fid |
| 3 | idx_t_im_mdc_sharedetail_a |  | fshdiffshareid |

---

## 领料差异分摊明细-主表 t_im_mdc_difsharedetail

- **表名称：** 领料差异分摊明细-主表
- **表名：** t_im_mdc_difsharedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdiffshareid | 领料差异分摊id | int8 | 64 |  | √ | 0 | 领料差异分摊id |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fdiffshareno | 领料差异分摊编号 | varchar | 50 |  | √ | ' ' | 领料差异分摊编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_im_mdc_difsharedetail |  | fdiffshareid |
| 2 | pk_im_mdc_difsharedetail |  | fid |
