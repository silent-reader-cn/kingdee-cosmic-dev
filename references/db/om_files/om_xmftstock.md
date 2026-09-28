# 委外用料清单变更单-om_xmftstock

## 物料明细-分表 t_om_xmftstockentry_b

- **表名称：** 物料明细-分表
- **表名：** t_om_xmftstockentry_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbusdenominator | 分母 | numeric | 23 | 10 | √ | 0 | 分母 |
| 2 | fbusbadincomerejectedqty | 来料不良退料数量 | numeric | 23 | 10 | √ | 0 | 来料不良退料数量 |
| 3 | funissueqty | 未领基本数量 | numeric | 23 | 10 | √ | 0 | 未领基本数量 |
| 4 | foutqty | 关联领料基本数量 | numeric | 23 | 10 | √ | 0 | 关联领料基本数量 |
| 5 | fallotqty | 基本单位.已调拨数量 | numeric | 23 | 10 | √ | 0 | 基本单位.已调拨数量 |
| 6 | fbusgoodrejectedqty | 良品退料数量 | numeric | 23 | 10 | √ | 0 | 良品退料数量 |
| 7 | fwastagerateformula | 损耗计算公式 | varchar | 50 |  | √ | ' ' | 损耗计算公式,枚举: A :标准用量/（1-损耗率） B :标准用量*（1+损耗率） |
| 8 | fstandqty | 标准基本数量 | numeric | 23 | 10 | √ | 0 | 标准基本数量 |
| 9 | fbadtaskrejectedqty | 作业不良退料基本数量 | numeric | 23 | 10 | √ | 0 | 作业不良退料基本数量 |
| 10 | fgoodrejectedqty | 良品退料基本数量 | numeric | 23 | 10 | √ | 0 | 良品退料基本数量 |
| 11 | fscraprate | 变动损耗率% | numeric | 23 | 10 | √ | 0 | 变动损耗率% |
| 12 | ffeedingqty | 补料基本数量 | numeric | 23 | 10 | √ | 0 | 补料基本数量 |
| 13 | finvmatunitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | fbusactissueqty | 已领数量 | numeric | 23 | 10 | √ | 0 | 已领数量 |
| 15 | fuseqty | 已消耗基本数量 | numeric | 23 | 10 | √ | 0 | 已消耗基本数量 |
| 16 | fbadincomerejectedqty | 来料不良退料基本数量 | numeric | 23 | 10 | √ | 0 | 来料不良退料基本数量 |
| 17 | factissueqty | 已领基本数量 | numeric | 23 | 10 | √ | 0 | 已领基本数量 |
| 18 | fownertype | 产品货主类型 | varchar | 30 |  | √ | ' ' | 产品货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 19 | fbusbadtaskrejectedqty | 作业不良退料数量 | numeric | 23 | 10 | √ | 0 | 作业不良退料数量 |
| 20 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 21 | fbusstandqty | 标准数量 | numeric | 23 | 10 | √ | 0 | 标准数量 |
| 22 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 23 | fisjumplevel | 跳层 | bpchar | 1 |  | √ | '0' | 跳层 |
| 24 | fbusoutqty | 关联领料数量 | numeric | 23 | 10 | √ | 0 | 关联领料数量 |
| 25 | fbususeqty | 已消耗数量 | numeric | 23 | 10 | √ | 0 | 已消耗数量 |
| 26 | fbusunissueqty | 未领数量 | numeric | 23 | 10 | √ | 0 | 未领数量 |
| 27 | fuseratio | 使用比例(%) | numeric | 23 | 10 | √ | 0 | 使用比例(%) |
| 28 | fscrapqty | 报废基本数量 | numeric | 23 | 10 | √ | 0 | 报废基本数量 |
| 29 | fqtydenominator | 基本单位分母 | numeric | 23 | 10 | √ | 0 | 基本单位分母 |
| 30 | fqtynumerator | 基本单位分子 | numeric | 23 | 10 | √ | 0 | 基本单位分子 |
| 31 | fbusdemandqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 32 | fchildmatunitid | 子项单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 33 | frejectedqty | 退料基本数量 | numeric | 23 | 10 | √ | 0 | 退料基本数量 |
| 34 | fsrctype | 子项来源类型 | bpchar | 1 |  | √ | 'A' | 子项来源类型,枚举: A :普通 B :补料单反写 C :退料单反写 |
| 35 | fbusnumerator | 分子 | numeric | 23 | 10 | √ | 0 | 分子 |
| 36 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0 | 固定损耗 |
| 37 | fownerid | 产品货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | fwipqty | 在制基本数量 | numeric | 23 | 10 | √ | 0 | 在制基本数量 |
| 39 | fpushdownmatqty | 下推领料数量 | numeric | 23 | 10 | √ | 0 | 下推领料数量 |
| 40 | fchildmatunitqty | 子项单位数量 | numeric | 23 | 10 | √ | 0 | 子项单位数量 |
| 41 | fdemandqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 42 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 43 | fcansendqty | 可领基本数量 | numeric | 23 | 10 | √ | 0 | 可领基本数量 |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_xmftstockentry_b |  | fdetailid |
| 2 | idx_om_xmftstockentry_b |  | fentryid |

---

## 关联子实体-子表 t_om_mftstock_lk

- **表名称：** 关联子实体-子表
- **表名：** t_om_mftstock_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_mftstock_lk |  | fpkid |
| 2 | idx_om_mftstock_lk_fk |  | fentryid |

---

## 物料明细-分表 t_om_xmftstockentry_a

- **表名称：** 物料明细-分表
- **表名：** t_om_xmftstockentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fislead | 是否引入 | bpchar | 1 |  | √ | '0' | 是否引入 |
| 2 | fstockentryseq | 委外用料清单行号 | varchar | 50 |  | √ | ' ' | 委外用料清单行号 |
| 3 | fproducttransid | 委外事务类型 | int8 | 64 |  | √ | 0 | 生产事务类型 mpdm_transactproduct |
| 4 | fentryorderno | 委外工单编号 | varchar | 50 |  | √ | ' ' | 委外工单编号 |
| 5 | ftransdictrelqty | 子项单位.调拨关联数量 | numeric | 23 | 10 | √ | 0 | 子项单位.调拨关联数量 |
| 6 | ftransdictqty | 子项单位.已调拨数量 | numeric | 23 | 10 | √ | 0 | 子项单位.已调拨数量 |
| 7 | fqcppbaseqty | 退料请检完成基本数量 | numeric | 23 | 10 | √ | 0 | 退料请检完成基本数量 |
| 8 | fstockno | 委外用料清单编号 | varchar | 50 |  | √ | ' ' | 委外用料清单编号 |
| 9 | freplacegroup | 替代组号 | int8 | 64 |  | √ | 0 | 替代组号 |
| 10 | fisreturninspect | 委外退料检验 | bpchar | 1 |  | √ | 0 | 委外退料检验 |
| 11 | fqcppbasejoinqty | 退料请检关联基本数量 | numeric | 23 | 10 | √ | 0 | 退料请检关联基本数量 |
| 12 | fbasetransapplyqty | 基本单位.调拨申请数量 | numeric | 23 | 10 | √ | 0 | 基本单位.调拨申请数量 |
| 13 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 14 | fqcppqty | 退料请检完成数量 | numeric | 23 | 10 | √ | 0 | 退料请检完成数量 |
| 15 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 17 | fproductno | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 18 | fqcppjoinqty | 退料请检关联数量 | numeric | 23 | 10 | √ | 0 | 退料请检关联数量 |
| 19 | ftransapplyrelqty | 子项单位.调拨申请关联数量 | numeric | 23 | 10 | √ | 0 | 子项单位.调拨申请关联数量 |
| 20 | fprodeptorgid | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fparentid | 父ID | int8 | 64 |  | √ | 0 | 父ID |
| 22 | fbusrejectedqty | 退料数量 | numeric | 23 | 10 | √ | 0 | 退料数量 |
| 23 | fentryidf | 组件清单分录f7 | int8 | 64 |  | √ | 0 | 委外用料清单分录f7 om_mftstockf7 |
| 24 | fproductbaseunit | 产品基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | ftransapplyqty | 子项单位.调拨申请数量 | numeric | 23 | 10 | √ | 0 | 子项单位.调拨申请数量 |
| 26 | fstockid | 委外组件清单ID | varchar | 50 |  | √ | ' ' | 委外组件清单ID |
| 27 | fbuswipqty | 在制数量 | numeric | 23 | 10 | √ | 0 | 在制数量 |
| 28 | fbusfeedingqty | 补料数量 | numeric | 23 | 10 | √ | 0 | 补料数量 |
| 29 | fentryorderentryid | 委外工单行id | int8 | 64 |  | √ | 0 | 委外工单分录F7 om_mftorder_f7 |
| 30 | finvtransdictqty | 库存单位.已调拨数量 | numeric | 23 | 10 | √ | 0 | 库存单位.已调拨数量 |
| 31 | ftotalleadtime | 总提前期偏置(天) | numeric | 23 | 10 | √ | 0 | 总提前期偏置(天) |
| 32 | fstockentryid | 委外组件清单分录ID | varchar | 50 |  | √ | ' ' | 委外组件清单分录ID |
| 33 | fbasetransapplyrelqty | 基本单位.调拨申请关联数量 | numeric | 23 | 10 | √ | 0 | 基本单位.调拨申请关联数量 |
| 34 | ftransdictnonqty | 子项单位.未调拨数量 | numeric | 23 | 10 | √ | 0 | 子项单位.未调拨数量 |
| 35 | fbasetransdictrelqty | 基本单位.调拨关联数量 | numeric | 23 | 10 | √ | 0 | 基本单位.调拨关联数量 |
| 36 | fbuscansendqty | 可领数量 | numeric | 23 | 10 | √ | 0 | 可领数量 |
| 37 | fbusallotqty | 调拨数量 | numeric | 23 | 10 | √ | 0 | 调拨数量 |
| 38 | fbusscrapqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 39 | fprovideorgid | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fproductbaseqty | 产品基本数量 | numeric | 23 | 10 | √ | 0 | 产品基本数量 |
| 41 | fbasetransdictnonqty | 基本单位.未调拨数量 | numeric | 23 | 10 | √ | 0 | 基本单位.未调拨数量 |
| 42 | finvtransdictnonqty | 库存单位.未调拨数量 | numeric | 23 | 10 | √ | 0 | 库存单位.未调拨数量 |
| 43 | finvtransdictrelqty | 库存单位.调拨关联数量 | numeric | 23 | 10 | √ | 0 | 库存单位.调拨关联数量 |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 45 | fentrychangetype | 变更方式 | varchar | 50 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :取消 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_xoeta_stockno |  | fstockno |
| 2 | pk_om_xmftstockentry_a |  | fdetailid |
| 3 | idx_om_xmftstockentry_a |  | fentryid |
| 4 | idx_om_xmftstockentry_a_eoeid |  | fentryorderentryid |

---

## 委外用料清单变更单-主表 t_om_xmftorderentry_s

- **表名称：** 委外用料清单变更单-主表
- **表名：** t_om_xmftorderentry_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 委外工单主id | int8 | 64 |  | √ | 0 | 委外工单主id |
| 2 | fbillauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 3 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 4 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | forderid | 委外工单ID | varchar | 50 |  | √ | ' ' | 委外工单ID |
| 6 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fconfiguredcodeid | 产品配置号(废弃) | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 8 | forderentryid | 委外工单行号 | int8 | 64 |  | √ | 0 | 委外工单分录F7 om_mftorder_f7 |
| 9 | fbiztime | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 10 | fisinit | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fomversion | BOM版本 | varchar | 50 |  | √ | ' ' | BOM版本 |
| 13 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 14 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 15 | freplaceno | 替代号 | varchar | 50 |  | √ | ' ' | 替代号 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 18 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 19 | fbaseunitid | 产品基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | fplanpreparetime | 计划准备时间 | timestamp | 0 |  |  | null | 计划准备时间 |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | ftransactiontypeid | ftransactiontypeid | int8 | 64 |  | √ | 0 |  |
| 23 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fischanged | 是否存在未审核变更单 | bpchar | 1 |  | √ | '0' | 是否存在未审核变更单 |
| 26 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 29 | fproductmasterid | 产品(主数据) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 30 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 31 | fmftdeptorgid | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | freason | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 33 | freasonid | 变更原因 | int8 | 64 |  | √ | 0 | 变更原因 pdm_ecnreason |
| 34 | forderno | 委外工单编号 | varchar | 50 |  | √ | ' ' | 委外工单编号 |
| 35 | fprocessroute | 工艺路线 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 36 | fmftinqty | 最新完工入库数量 | numeric | 23 | 10 | √ | 0 | 最新完工入库数量 |
| 37 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 38 | fsuppliertop | 委外加工商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 39 | fbaseqty | 产品基本数量 | numeric | 23 | 10 | √ | 0 | 产品基本数量 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | fbillauxunit | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 43 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_xoet_orderno |  | forderno |
| 2 | idx_om_xoet_orgfid |  | forgid,fid |
| 3 | pk_om_xmftorderentry_s |  | fentryid |
| 4 | idx_om_xmftorderentry_s |  | fbillno |
| 5 | idx_om_xoet_createtime |  | fcreatetime |

---

## 委外用料清单变更单-反写记录表 t_om_mftstock_wb

- **表名称：** 委外用料清单变更单-反写记录表
- **表名：** t_om_mftstock_wb

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
| 1 | idx_om_mftstock_wb_fk |  | fid |
| 2 | pk_om_mftstock_wb |  | fentryid |

---

## 委外用料清单变更单-多语言表 t_om_xmftorderentry_s_l

- **表名称：** 委外用料清单变更单-多语言表
- **表名：** t_om_xmftorderentry_s_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_xmftorderentry_s_l |  | fpkid |
| 2 | idx_om_xmftorderentry_s_l_0 |  | fentryid,flocaleid |

---

## 关联子实体-子表 t_om_mftstockentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_om_mftstockentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_mftstockentry_lk |  | fpkid |
| 2 | idx_om_mftstockentry_lk_fk |  | fdetailid |

---

## 物料明细-子表 t_om_xmftstockentry

- **表名称：** 物料明细-子表
- **表名：** t_om_xmftstockentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbomreversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 2 | fmaterielinv | 物料库存信息 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 3 | fentryproductnanme | fentryproductnanme | varchar | 50 |  | √ | ' ' |  |
| 4 | fissuemode | 领送料方式 | varchar | 50 |  | √ | ' ' | 领送料方式,枚举: A :生产领料 B :直送 C :不领料 |
| 5 | fbackflushtime | 倒冲时机 | varchar | 50 |  | √ | ' ' | 倒冲时机,枚举: A :入库倒冲 B :收货倒冲 |
| 6 | fiscannegative | 退料 | bpchar | 1 |  | √ | '0' | 退料 |
| 7 | flocation | 发料仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | foutlocation | 调出仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 10 | fdemanddate | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 11 | fchildauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 12 | fsupplier | 委外供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 13 | fworkplanid | 工序计划分录ID | int8 | 64 |  | √ | 0 | 工序计划分录ID |
| 14 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 15 | fisstockallot | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fissinlowlimit | 领料下限允差(%) | numeric | 10 | 2 | √ | 0 | 领料下限允差(%) |
| 18 | frework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 19 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 20 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 21 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 22 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 23 | fchildbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 24 | fwarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 25 | fsupplierid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fiskeypart | 关键件 | bpchar | 1 |  | √ | '0' | 关键件 |
| 27 | fworkstation | 工位 | int8 | 64 |  | √ | 0 | 工位 mpdm_workstation |
| 28 | fisstep | 是否阶梯用量 | bpchar | 1 |  | √ | '0' | 是否阶梯用量 |
| 29 | foprworkcenter | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 30 | fsupplymode | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :委外加工商 |
| 31 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 32 | foperationdesc | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 33 | fmaterialunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 34 | fchildbomversion | 子项BOM版本 | varchar | 50 |  | √ | ' ' | 子项BOM版本 |
| 35 | fsupplyorgid | 发料组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fextraratioqty | 领料上限基本数量 | numeric | 23 | 10 | √ | 0 | 领料上限基本数量 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 38 | fprocessseq | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 39 | freservebaseqty | 库存预留基本数量 | numeric | 23 | 10 | √ | 0 | 库存预留基本数量 |
| 40 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 41 | fpriority | 替代优先级 | int8 | 64 |  | √ | 0 | 替代优先级 |
| 42 | fconfiguredcodeid | 产品配置号(废弃) | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 43 | fentryconfiguredcodeid | 组件配置号(废弃) | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 44 | fsentryseq | fsentryseq | varchar | 50 |  | √ | ' ' |  |
| 45 | fpromaterentryid | 工序物料分配分录ID | int8 | 64 |  | √ | 0 | 工序物料分配分录ID |
| 46 | fmaterielmasterid | 物料(主数据) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 47 | freplaceplan | 物料替代方案 | int8 | 64 |  | √ | 0 | 物料替代方案 mpdm_replaceplan |
| 48 | fmachiningtype | 加工类型 | varchar | 50 |  | √ | ' ' | 加工类型,枚举: 1001 :厂内加工 1002 :委外加工 1003 :内协加工 1004 :不限制 |
| 49 | foprno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 50 | fisbomextend | 来源于BOM展开 | bpchar | 1 |  | √ | '0' | 来源于BOM展开 |
| 51 | fworkprocedureid | 工序编码 | int8 | 64 |  | √ | 0 | 标准工序定义(废弃) mpdm_workprocedure |
| 52 | fbomentryid | BOM分录ID | int8 | 64 |  | √ | 0 | BOM分录ID |
| 53 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 54 | foutorgunitid | 调出库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 55 | fleadtime | 提前期偏置(天) | numeric | 23 | 10 | √ | 0 | 提前期偏置(天) |
| 56 | foverissuecontrl | 超发控制 | varchar | 50 |  | √ | ' ' | 超发控制,枚举: A :可超发 B :不可超发 C :最小包装量 |
| 57 | fissinhighlimit | 领料上限允差(%) | numeric | 10 | 2 | √ | 0 | 领料上限允差(%) |
| 58 | favbbaseqty | 库存可用基本数量 | numeric | 23 | 10 | √ | 0 | 库存可用基本数量 |
| 59 | fqtytype | 用量类型 | varchar | 50 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :变动 |
| 60 | fismainreplace | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 61 | fisbackflush | 倒冲 | varchar | 50 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :始终倒冲 C :工作中心决定是否倒冲 |
| 62 | flackraitioqty | 领料下限基本数量 | numeric | 23 | 10 | √ | 0 | 领料下限基本数量 |
| 63 | fsrcbillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 64 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 65 | fisbulkmaterial | 散装物料 | bpchar | 1 |  | √ | '0' | 散装物料 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_xmftstockentry |  | fdetailid |
| 2 | idx_om_xmftstockentry_fk |  | fentryid |
| 3 | idx_om_xoentry_materialid |  | fmaterielmasterid |

---

## 委外用料清单变更单-关联追踪表 t_om_mftstock_tc

- **表名称：** 委外用料清单变更单-关联追踪表
- **表名：** t_om_mftstock_tc

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
| 1 | idx_om_mftstock_tc_tid |  | ftid |
| 2 | pk_om_mftstock_tc |  | fid |
| 3 | idx_om_mftstock_tc_tbill |  | ftbillid |

---

## 物料明细-多语言表 t_om_xmftstockentry_l

- **表名称：** 物料明细-多语言表
- **表名：** t_om_xmftstockentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 3 | fchildremarks | 备注 | varchar | 250 |  | √ | ' ' | 备注 |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |
| 5 | fsetuplocation | 安装位置 | varchar | 100 |  | √ | ' ' | 安装位置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_xmftstockentry_l_0 |  | fdetailid,flocaleid |
| 2 | pk_om_xmftstockentry_l |  | fpkid |
