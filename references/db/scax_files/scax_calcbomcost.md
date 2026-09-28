# 模拟卷算结果-scax_calcbomcost

## 模拟卷算结果-主表 t_scax_calcbomcost

- **表名称：** 模拟卷算结果-主表
- **表名：** t_scax_calcbomcost

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcalctaskrecord | 卷算任务 | int8 | 64 |  | √ | 0 | [标准成本任务 sco_task](../sco_files/sco_task.md) |
| 6 | fcalckeycol | 卷算维度 | int8 | 64 |  | √ | 0 | [卷算维度数据表 sco_keycol](../sco_files/sco_keycol.md) |
| 7 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 8 | froute | 工艺路线 | int8 | 64 |  | √ | 0 | [成本工艺路线 scax_costroute](../scax_files/scax_costroute.md) |
| 9 | fcalcdate | 卷算日期 | timestamp | 0 |  |  | null | 卷算日期 |
| 10 | fproducttype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: 1 :主产品 10720 :联产品 10730 :副产品 |
| 11 | funitcost | 单位总成本 | numeric | 23 | 10 | √ | 0 | 单位总成本 |
| 12 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 13 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fcosttype | 标准成本方案 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 16 | fmatcalcprop | 物料卷算属性 | varchar | 30 |  | √ | ' ' | 物料卷算属性,枚举: A :自制 B :外购 C :委外 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fcostbom | 成本BOM | int8 | 64 |  | √ | 0 | [成本BOM scax_costbom](../scax_files/scax_costbom.md) |
| 19 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 20 | funit | 单位 | varchar | 30 |  | √ | ' ' | 单位,枚举: 1 :时 2 :分 3 :秒 |

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
| 3 | fparentmaterial | 父物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | flayer | 半成品卷算所在层级 | int4 | 32 |  | √ | 0 | 半成品卷算所在层级 |
| 5 | fparentlayerlevel | 复合级次父级 | varchar | 4000 |  | √ | ' ' | 复合级次父级 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | felement | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 8 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 9 | flayerlevel | 复合级次 | int4 | 32 |  | √ | 0 | 复合级次 |
| 10 | fcalcbomkeycol | 卷算维度 | int8 | 64 |  | √ | 0 | [卷算维度数据表 sco_keycol](../sco_files/sco_keycol.md) |
| 11 | fsubelement | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 12 | fmaterial | 子项物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 13 | fcalcbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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
| 2 | fprocesssequence | 序列号 | int4 | 32 |  | √ | 0 | 序列号 |
| 3 | fsrcbillsupid | 价格来源供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 4 | fchildbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | felement | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 7 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 8 | flayerlevel | 复合级次 | int4 | 32 |  | √ | 0 | 复合级次 |
| 9 | fsrcbillentryseq | 价格来源单据分录行号 | int4 | 32 |  | √ | 0 | 价格来源单据分录行号 |
| 10 | fprocessinstructions | 工序说明 | varchar | 512 |  | √ | ' ' | 工序说明 |
| 11 | fsrcbillsupnumber | 价格来源单据供应商 | varchar | 255 |  | √ | ' ' | 价格来源单据供应商 |
| 12 | fprocesscode | 工序编码 | int8 | 64 |  | √ | 0 | [标准工序 mpdm_normprocess](../mpdm_files/mpdm_normprocess.md) |
| 13 | fsubelement | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 14 | fmaterial | 子项物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 15 | fprocessnumber | 工序号 | int4 | 32 |  | √ | 0 | 工序号 |
| 16 | fchildcalckeycol | 卷算维度 | int8 | 64 |  | √ | 0 | [卷算维度数据表 sco_keycol](../sco_files/sco_keycol.md) |
| 17 | fqty | 耗用数量 | numeric | 23 | 10 | √ | 0 | 耗用数量 |
| 18 | fsrcbillnumber | 价格来源单据编码 | varchar | 255 |  | √ | ' ' | 价格来源单据编码 |
| 19 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 20 | fdatasrc | 数据来源 | varchar | 100 |  | √ | ' ' | 数据来源,枚举: manual :手工新增 contract :采购合同 order :采购订单 purchase :采购价目表 cal_balance :核算余额表 |
| 21 | fworksrc | 作业来源 | varchar | 255 |  | √ | ' ' | 作业来源,枚举: 0 :机器 1 :人工 |
| 22 | fworkpriceid | 作业价格维护 | int8 | 64 |  | √ | 0 | 作业价格维护 scax_mftworkprice |
| 23 | fworktypeid | 作业类型 | int8 | 64 |  | √ | 0 | [作业类型 scax_worktype](../scax_files/scax_worktype.md) |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fprocesscenter | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心 sfc_workcenter](../mpdm_files/sfc_workcenter.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scax_childcostdetail |  | fentryid |
