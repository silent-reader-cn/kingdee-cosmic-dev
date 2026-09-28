# 归集报告-sco_colreport

## 单据体-子表 t_sco_colreportdiffentry

- **表名称：** 单据体-子表
- **表名：** t_sco_colreportdiffentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmftorg | fmftorg | int8 | 64 |  | √ | 0 |  |
| 3 | fsrcbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 4 | fproducedeptid | fproducedeptid | int8 | 64 |  | √ | 0 |  |
| 5 | fmfttransaction | fmfttransaction | int8 | 64 |  | √ | 0 |  |
| 6 | fsrcbiztype | fsrcbiztype | int8 | 64 |  | √ | 0 |  |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fsrcinvscheme | fsrcinvscheme | int8 | 64 |  | √ | 0 |  |
| 9 | freason | 原因分析 | varchar | 2000 |  | √ | ' ' | 原因分析 |
| 10 | fworkcenter | fworkcenter | int8 | 64 |  | √ | 0 |  |
| 11 | fsrcseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 12 | fsrcbillstatus | fsrcbillstatus | varchar | 30 |  | √ | ' ' |  |
| 13 | fproductworkshopid | fproductworkshopid | int8 | 64 |  | √ | 0 |  |
| 14 | fcomparedate | 源单日期 | timestamp | 0 |  |  | null | 源单日期 |
| 15 | fmftstatus | fmftstatus | varchar | 30 |  | √ | ' ' |  |
| 16 | fsrcbilltype | 单据类型 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型,枚举: mftorder :生产工单 outorder :委外工单 changelog :变更单 splitlog :拆分单 wgrk :完工入/退库单 wwwgrk :委外完工入/退库单 scrk :生产入/退库单 scll :生产领/退/补料单 wwll :委外领/退/补料单 llck :领料出库单 gxhb :工序汇报单 gdhb :工单汇报单 hbzytz :汇报资源调整单 wwgxhb :委外工序汇报单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_colreportdiffentry |  | fentryid |
| 2 | idx_sco_colreportdiffentry |  | fid |

---

## 来源行政组织-多选基础资料表 t_sco_collogobjag

- **表名称：** 来源行政组织-多选基础资料表
- **表名：** t_sco_collogobjag

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 行政组织（部门） bos_adminorg |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_collogobjag |  | fpkid |
| 2 | idx_sco_collogobjag |  | fentryid |

---

## 归集报告-主表 t_sco_colreport

- **表名称：** 归集报告-主表
- **表名：** t_sco_colreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcoldate | 归集日期 | timestamp | 0 |  |  | null | 归集日期 |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcolobj | 归集对象 | varchar | 30 |  | √ | ' ' | 归集对象,枚举: costobject :成本核算对象 plan :计划生产数量 factned :完工 mat :材料耗用 resource :资源 workhoursfee :工时耗用 mfgfee :制造费用 |
| 8 | fappnum | 业务标识 | varchar | 10 |  | √ | ' ' | 业务标识 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | faudittime | faudittime | timestamp | 0 |  |  | null |  |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | ferror | 存在差异或异常 | bpchar | 1 |  | √ | '0' | 存在差异或异常 |
| 13 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 15 | fdaterange | 归集时间范围 | varchar | 80 |  | √ | ' ' | 归集时间范围 |
| 16 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_colreport |  | fid |
| 2 | idx_sco_colreport |  | forgid,fbillno |

---

## 来源工作中心-多选基础资料表 t_sco_collogobjwc

- **表名称：** 来源工作中心-多选基础资料表
- **表名：** t_sco_collogobjwc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_collogobjwc |  | fentryid |
| 2 | pk_sco_collogobjwc |  | fpkid |

---

## 来源供应商-多选基础资料表 t_sco_collogobjsupplier

- **表名称：** 来源供应商-多选基础资料表
- **表名：** t_sco_collogobjsupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_collogobjsupplier |  | fentryid |
| 2 | pk_sco_collogobjsupplier |  | fpkid |

---

## 不归集生产事务类型-多选基础资料表 t_sco_colreport_tran

- **表名称：** 不归集生产事务类型-多选基础资料表
- **表名：** t_sco_colreport_tran

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 生产事务类型 mpdm_transactproduct |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_colreport_tran |  | fpkid |
| 2 | idx_sco_colreport_tran |  | fid |

---

## 不归集库存事务-多选基础资料表 t_sco_colreport_invscheme

- **表名称：** 不归集库存事务-多选基础资料表
- **表名：** t_sco_colreport_invscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_colreport_invscheme |  | fpkid |
| 2 | idx_sco_colreport_inv |  | fid |

---

## 不归集业务类型-多选基础资料表 t_sco_colreport_biztype

- **表名称：** 不归集业务类型-多选基础资料表
- **表名：** t_sco_colreport_biztype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_colreport_biztype |  | fpkid |
| 2 | idx_sco_colreport_biztype |  | fid |

---

## 单据体-子表 t_sco_colrptconfigentry

- **表名称：** 单据体-子表
- **表名：** t_sco_colrptconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostcenter | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 3 | fcolrange | 归集单据范围 | varchar | 50 |  | √ | ' ' | 归集单据范围,枚举: SCGD :生产工单 WWGD :委外工单 WGRK :完工入库数量归集单 WIPCOMPELETE :完工入/退库单 WWGRK :委外完工入/退库单 PRODUCTCOMPELETE :生产入/退库单 PRO_GET :生产领/退/补料单 GET_OUTSTORAGE :领料出库单 WLL :委外领/退/补料单 PROCESSREPORT :工序汇报单 PROCESSADJUST :汇报资源调整单 MFTORDERREPORT :工单汇报单 WGXHB :委外工序汇报单 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fcaltype | 成本计算方法 | varchar | 50 |  | √ | ' ' | 成本计算方法 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_colrptconfigentry |  | fentryid |
| 2 | idx_sco_colrptconfigentry |  | fid |

---

## 步骤明细-子表 t_sco_colreportentry

- **表名称：** 步骤明细-子表
- **表名：** t_sco_colreportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstep | 详细步骤 | varchar | 50 |  | √ | ' ' | 详细步骤 |
| 3 | ftip | 提示 | varchar | 255 |  | √ | ' ' | 提示 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fresult | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :未执行 2 :执行中 3 :失败 4 :成功 5 :通过 6 :不通过 7 :提醒 |
| 6 | fcostime | 耗时（毫秒） | varchar | 50 |  | √ | ' ' | 耗时（毫秒） |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ftip_tag | 提示_详情 | text | 0 |  |  | null | 提示_详情 |
| 9 | fcheckdesc | 归集结果 | varchar | 255 |  | √ | ' ' | 归集结果 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_colreportentry |  | fid |
| 2 | pk_sco_colreportentry |  | fentryid |

---

## 来源业务单元-多选基础资料表 t_sco_collogobjorg

- **表名称：** 来源业务单元-多选基础资料表
- **表名：** t_sco_collogobjorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_collogobjorg |  | fpkid |
| 2 | idx_sco_collogobjorg |  | fentryid |
