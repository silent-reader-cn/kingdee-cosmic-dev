# 模拟卷算结果-scax_calcbomcost

## 模拟卷算结果-主表 t_scax_calcbomcost

- **表名称：** 模拟卷算结果-主表
- **表名：** t_scax_calcbomcost

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcalctaskrecord | 卷算任务 | int8 | 64 |  | √ | 0 | 卷算报告 scax_calctaskrecord |
| 6 | fcalckeycol | 卷算维度 | int8 | 64 |  | √ | 0 | 卷算维度数据表 sco_keycol |
| 7 | froute | 工艺路线 | int8 | 64 |  | √ | 0 | 成本工艺路线 scax_costroute |
| 8 | fcalcdate | 卷算日期 | timestamp | 0 |  |  | null | 卷算日期 |
| 9 | fproducttype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: 1 :主产品 10720 :联产品 10730 :副产品 |
| 10 | funitcost | 单位总成本 | numeric | 23 | 10 | √ | 0 | 单位总成本 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcosttype | 标准成本方案 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 13 | fmatcalcprop | 物料卷算属性 | varchar | 30 |  | √ | ' ' | 物料卷算属性,枚举: A :自制 B :外购 C :委外 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fcostbom | 成本BOM | int8 | 64 |  | √ | 0 | 成本BOM scax_costbom |
| 16 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 17 | funit | 单位 | varchar | 30 |  | √ | ' ' | 单位,枚举: 1 :时 2 :分 3 :秒 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scax_calcbomcost |  | fcosttype,fmaterial |
| 2 | pk_scax_calcbomcost |  | fid |

---

## 半成品耗用详情-子表 t_scax_calcbomdetail

- **表名称：** 半成品耗用详情-子表
- **表名：** t_scax_calcbomdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 耗用数量 | numeric | 23 | 10 | √ | 0 | 耗用数量 |
| 3 | fcalcbomkeycol | 卷算维度 | int8 | 64 |  | √ | 0 | 卷算维度数据表 sco_keycol |
| 4 | fparentmaterial | 父物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | flayer | 半成品卷算所在层级 | int4 | 32 |  | √ | 0 | 半成品卷算所在层级 |
| 6 | fparentlayerlevel | 复合级次父级 | varchar | 4000 |  | √ | ' ' | 复合级次父级 |
| 7 | fsubelement | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fmaterial | 子项物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 10 | felement | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | flayerlevel | 复合级次 | int4 | 32 |  | √ | 0 | 复合级次 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scax_calcbomdetail |  | fentryid |
| 2 | idx_scax_calcbomdetail |  | fid |

---

## 单据体-子表 t_scax_childcostdetail

- **表名称：** 单据体-子表
- **表名：** t_scax_childcostdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 耗用数量 | numeric | 23 | 10 | √ | 0 | 耗用数量 |
| 3 | fprocesssequence | 序列号 | int4 | 32 |  | √ | 0 | 序列号 |
| 4 | fsrcbillnumber | 价格来源单据编码 | varchar | 255 |  | √ | ' ' | 价格来源单据编码 |
| 5 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdatasrc | 数据来源 | varchar | 10 |  | √ | ' ' | 数据来源,枚举: manual :手工新增 contract :采购合同 order :采购订单 purchase :采购价目表 |
| 8 | felement | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 9 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 10 | flayerlevel | 复合级次 | int4 | 32 |  | √ | 0 | 复合级次 |
| 11 | fsrcbillentryseq | 价格来源单据分录行号 | int4 | 32 |  | √ | 0 | 价格来源单据分录行号 |
| 12 | fprocesscode | 工序编码 | int8 | 64 |  | √ | 0 | 标准工序 mpdm_normprocess |
| 13 | fsubelement | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 14 | fmaterial | 子项物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 15 | fprocessnumber | 工序号 | int4 | 32 |  | √ | 0 | 工序号 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fprocesscenter | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心 sfc_workcenter |
| 18 | fchildcalckeycol | 卷算维度 | int8 | 64 |  | √ | 0 | 卷算维度数据表 sco_keycol |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scax_childcostdetail |  | fentryid |
