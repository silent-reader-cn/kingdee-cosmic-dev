# 检修工单-pom_mroorder

## 检修工单-主表 t_pom_mroorder

- **表名称：** 检修工单-主表
- **表名：** t_pom_mroorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fswsnum | 补充工作单数量 | int8 | 64 |  | √ | 0 | 补充工作单数量 |
| 4 | ftransactiontype | ftransactiontype | int8 | 64 |  | √ | 0 |  |
| 5 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 6 | fentitytype | 单据实体类型 | varchar | 50 |  | √ | ' ' | 单据实体类型,枚举: pom_mroorder :检修工单 pom_mronrc :非例行工卡 pom_mropartcard :零部件工卡 pom_mrosupportcard :支援工卡 |
| 7 | fbillnonew | fbillnonew | varchar | 50 |  | √ | ' ' |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fattachmentcount | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
| 10 | fbiztype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体,枚举: pom_mrosws :补充工作单 |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fbilltypenew | fbilltypenew | int8 | 64 |  | √ | 0 |  |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :作废 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 20 | fnumberautogen | 编码自动生成 | bpchar | 1 |  | √ | '0' | 编码自动生成 |
| 21 | fdailyexptype | 日常任务类型 | int8 | 64 |  | √ | 0 | 日常任务定义 mpdm_dailyexptypedef |
| 22 | fisgentoelecbill | 是否生成检修控制单 | bpchar | 1 |  | √ | '0' | 是否生成检修控制单 |
| 23 | fprintcount | 打印次数 | int8 | 64 |  | √ | 0 | 打印次数 |
| 24 | fissuborder | 是否子工单 | bpchar | 1 |  | √ | '0' | 是否子工单 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 27 | fisshowlist | 是否检修工单列表显示 | bpchar | 1 |  | √ | '0' | 是否检修工单列表显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mroorder_fbillno |  | fbillno |
| 2 | pk_pom_mroorder |  | fid |

---

## 缺陷类型-多选基础资料表 t_pom_defecttype

- **表名称：** 缺陷类型-多选基础资料表
- **表名：** t_pom_defecttype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 缺陷类型 fmm_defecttype |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pom_defecttype |  | fpkid |
| 2 | idx_pom_defecttype_fk |  | fentryid |

---

## 项目任务-多选基础资料表 t_pom_mroprojecttask

- **表名称：** 项目任务-多选基础资料表
- **表名：** t_pom_mroprojecttask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 项目任务清单 pmts_task |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mroprojecttask_fk |  | fentryid |
| 2 | pk_pom_mroprojecttask |  | fpkid |

---

## 关联子实体-子表 t_pom_mroorderentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_mroorderentry_lk

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
| 1 | pk_pom_mroorderentry_lk |  | fpkid |
| 2 | idx_pom_mroorderentry_lk_fk |  | fentryid |

---

## 检修工单-关联追踪表 t_pom_mroorder_tc

- **表名称：** 检修工单-关联追踪表
- **表名：** t_pom_mroorder_tc

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
| 1 | pk_pom_mroorder_tc |  | fid |
| 2 | idx_pom_mroorder_tc_tid |  | ftid |
| 3 | idx_pom_mroorder_tc_tbill |  | ftbillid |

---

## 分录-分表 t_pom_mroorderentry_e

- **表名称：** 分录-分表
- **表名：** t_pom_mroorderentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facceptqty | 让步接收数量 | numeric | 23 | 10 | √ | 0 | 让步接收数量 |
| 3 | fisshortage | 材料存在短缺 | bpchar | 1 |  | √ | '0' | 材料存在短缺 |
| 4 | funquainwaqty | 不合格品入库基本数量 | numeric | 23 | 10 | √ | 0 | 不合格品入库基本数量 |
| 5 | fiscontrolqty | 控制入库数量 | bpchar | 1 |  | √ | '0' | 控制入库数量 |
| 6 | fswspageno | 补充工作单页码 | int8 | 64 |  | √ | 0 | 补充工作单页码 |
| 7 | fyieldrate | 成品率% | numeric | 23 | 10 | √ | 0 | 成品率% |
| 8 | fmtlcostqty | 料废数量 | numeric | 23 | 10 | √ | 0 | 料废数量 |
| 9 | fstockqty | 下推入库基本数量 | numeric | 23 | 10 | √ | 0 | 下推入库基本数量 |
| 10 | fcontrolno | 控制号 | varchar | 50 |  | √ | ' ' | 控制号 |
| 11 | froutereplace | 工艺路线替代号 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_routereplace |
| 12 | finwarconsigner | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fendcasetime | 齐套时间 | timestamp | 0 |  |  | null | 齐套时间 |
| 14 | fscrinwaqty | 报废品入库基本数量 | numeric | 23 | 10 | √ | 0 | 报废品入库基本数量 |
| 15 | frepminqty | 汇报下限数量 | numeric | 23 | 10 | √ | 0 | 汇报下限数量 |
| 16 | fappendixno | 附录编号 | varchar | 50 |  | √ | ' ' | 附录编号 |
| 17 | frepminrate | 汇报下限允差（%） | numeric | 23 | 10 | √ | 0 | 汇报下限允差（%） |
| 18 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 19 | fplanpreparetime | 计划准备时间 | timestamp | 0 |  |  | null | 计划准备时间 |
| 20 | ftarno | 技术文件编号 | varchar | 50 |  | √ | ' ' | 技术文件编号 |
| 21 | finwarmin | 入库下限基本数量 | numeric | 23 | 10 | √ | 0 | 入库下限基本数量 |
| 22 | freasonoferror | 出错原因 | varchar | 255 |  | √ | ' ' | 出错原因 |
| 23 | fpickingpairs | 已领套数 | numeric | 23 | 10 | √ | 0 | 已领套数 |
| 24 | funqualifiedqty | 不合格数量 | numeric | 23 | 10 | √ | 0 | 不合格数量 |
| 25 | fscrapqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 26 | fwaitcheckqty | 待检品入库数量 | numeric | 23 | 10 | √ | 0 | 待检品入库数量 |
| 27 | fisomtool | 外借工具 | bpchar | 1 |  | √ | '0' | 外借工具 |
| 28 | fworkwasteqty | 工废数量 | numeric | 23 | 10 | √ | 0 | 工废数量 |
| 29 | fquainwaqty | 合格品入库基本数量 | numeric | 23 | 10 | √ | 0 | 合格品入库基本数量 |
| 30 | frepairqty | 返修数量 | numeric | 23 | 10 | √ | 0 | 返修数量 |
| 31 | fmanuversion | 生产版本 | int8 | 64 |  | √ | 0 | 生产版本 pdm_manuversion |
| 32 | freworkqty | 返工数量 | numeric | 23 | 10 | √ | 0 | 返工数量 |
| 33 | farea | 工作区域 | int8 | 64 |  | √ | 0 | 工作区域 mpdm_area |
| 34 | fisinspection | 产品检验 | bpchar | 1 |  | √ | '0' | 产品检验 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 36 | frptqty | 下推汇报数量 | numeric | 23 | 10 | √ | 0 | 下推汇报数量 |
| 37 | fisfirstexe | 首次执行 | bpchar | 1 |  | √ | '0' | 首次执行 |
| 38 | frcvinhighlimit | 入库上限允差（%） | numeric | 23 | 10 | √ | 0 | 入库上限允差（%） |
| 39 | fisconreportqty | 控制汇报数量 | bpchar | 1 |  | √ | '0' | 控制汇报数量 |
| 40 | fplandays | 计划消耗天数 | int8 | 64 |  | √ | 0 | 计划消耗天数 |
| 41 | fmaterialspread | 重新展算订单物料 | bpchar | 1 |  | √ | '1' | 重新展算订单物料 |
| 42 | freplaceno | 替代号 | varchar | 50 |  | √ | ' ' | 替代号 |
| 43 | fsrcsplitbillnumber | 来源拆分工单编码 | varchar | 50 |  | √ | ' ' | 来源拆分工单编码 |
| 44 | frepmaxqty | 汇报上限数量 | numeric | 23 | 10 | √ | 0 | 汇报上限数量 |
| 45 | fisomexe | 外委执行 | bpchar | 1 |  | √ | '0' | 外委执行 |
| 46 | fqualifiedqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 47 | frepmaxrate | 汇报上限允差（%） | numeric | 23 | 10 | √ | 0 | 汇报上限允差（%） |
| 48 | fsrcsplitbillseq | 来源拆分工单行号 | int8 | 64 |  | √ | 0 | 生产工单分录F7模板 mpdm_mftorder_tplf7 |
| 49 | festscrapqty | 预计报废数量 | numeric | 23 | 10 | √ | 0 | 预计报废数量 |
| 50 | frepinwaqty | 返工品入库数量 | numeric | 23 | 10 | √ | 0 | 返工品入库数量 |
| 51 | fqualityorg | 质检组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 52 | frcvinlowlimit | 入库下限允差（%） | numeric | 23 | 10 | √ | 0 | 入库下限允差（%） |
| 53 | finwarmax | 入库上限基本数量 | numeric | 23 | 10 | √ | 0 | 入库上限基本数量 |
| 54 | freportqty | 汇报数量 | numeric | 23 | 10 | √ | 0 | 汇报数量 |
| 55 | fexpendbomtime | 展BOM时间 | timestamp | 0 |  |  | null | 展BOM时间 |
| 56 | foutputoperation | 产出工序 | int8 | 64 |  | √ | 0 | 标准工序定义(废弃) mpdm_workprocedure |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mroorderentry_e_fk |  | fid |
| 2 | pk_pom_mroorderentry_e |  | fentryid |

---

## 关联子实体-子表 t_pom_mroorder_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_mroorder_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_mroorder_lk |  | fpkid |
| 2 | idx_pom_mroorder_lk_fk |  | fid |

---

## 分录-子表 t_pom_mroorderentry

- **表名称：** 分录-子表
- **表名：** t_pom_mroorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanqty | 计划数量 | numeric | 23 | 10 | √ | 0 | 计划数量 |
| 3 | fdefectsiteid | 缺陷部位 | int8 | 64 |  | √ | 0 | 缺陷部位 fmm_defectsite |
| 4 | fmaterielinv | 物料库存信息 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 5 | fdisposalmeasuresid | 处置措施 | int8 | 64 |  | √ | 0 | 处置措施 fmm_disposalmeasures |
| 6 | flocation | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fworkcardid | 工卡 | int8 | 64 |  | √ | 0 | 工卡 mpdm_mrocardroute |
| 9 | fbdproject | 系统云项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 10 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fexecondition | 执行条件 | int8 | 64 |  | √ | 0 | 执行条件 mpdm_execondition |
| 12 | fclosetime | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 13 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 14 | fbomid | BOM | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 15 | fataid | 章节号 | int8 | 64 |  | √ | 0 | ATA章节号 mpdm_atachapterno |
| 16 | fpageseq | 页码 | varchar | 50 |  | √ | ' ' | 页码 |
| 17 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 18 | ftaskstatus | 任务状态 | varchar | 50 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 E :取消 F :保留 G :重下达 H :暂停 J :废弃 |
| 19 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 20 | fmanftechstatus | 工序计划状态 | varchar | 50 |  | √ | ' ' | 工序计划状态,枚举: T :存在工序计划 F :不存在工序计划 |
| 21 | fisassistmanual | 协助填写手册 | bpchar | 1 |  | √ | '0' | 协助填写手册 |
| 22 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 23 | fisom | 存在产品委外 | bpchar | 1 |  | √ | '0' | 存在产品委外 |
| 24 | fdefecttypeid | fdefecttypeid | int8 | 64 |  | √ | 0 |  |
| 25 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 26 | fplansuretime | 计划确认时间 | timestamp | 0 |  |  | null | 计划确认时间 |
| 27 | fstartworktime | 开工时间 | timestamp | 0 |  |  | null | 开工时间 |
| 28 | fsourcebilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 29 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 30 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 31 | fheadbillno | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 32 | fismajordefect | 是否重要结构缺陷 | bpchar | 1 |  | √ | '0' | 是否重要结构缺陷 |
| 33 | factualhours | 实际消耗工时 | numeric | 23 | 10 | √ | 0 | 实际消耗工时 |
| 34 | fprocessroute | 工艺路线编码 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 35 | fwarehouse | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 36 | fsourceentryseq | 来源单据分录行号 | varchar | 50 |  | √ | ' ' | 来源单据分录行号 |
| 37 | fmartype | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 38 | fbeginbookdate | 开工记账日期 | timestamp | 0 |  |  | null | 开工记账日期 |
| 39 | fplanbegintime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 40 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 41 | fwbsid | fwbsid | int8 | 64 |  | √ | 0 |  |
| 42 | fdefectdesc | 缺陷描述 | varchar | 500 |  | √ | ' ' | 缺陷描述 |
| 43 | fkittingstatus | 齐套状态 | varchar | 50 |  | √ | ' ' | 齐套状态,枚举: A :未检查 B :短缺 C :可用 |
| 44 | fmaterielmtc | 检修设备注册号 | int8 | 64 |  | √ | 0 | 物料检修信息 mpdm_materialmtcinfo |
| 45 | fworkstage | 工作类别 | int8 | 64 |  | √ | 0 | 工作类别 mpdm_workcategories |
| 46 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 47 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 48 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 49 | fassisterid | 协助者 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 50 | fzone | 功能位置 | int8 | 64 |  | √ | 0 | 功能位置 mpdm_functionlocation |
| 51 | fpriority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 52 | fata | 章节号(废弃) | varchar | 50 |  | √ | ' ' | 章节号(废弃) |
| 53 | fbizstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 C :关闭 |
| 54 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 55 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 56 | fmaterielmasterid | 物料(主数据) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 57 | fclosebookdate | 关闭记账日期 | timestamp | 0 |  |  | null | 关闭记账日期 |
| 58 | finwardept | 入库组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 59 | fpickstatus | 领料状态 | varchar | 50 |  | √ | ' ' | 领料状态,枚举: A :未领料 B :部分领料 C :全部领料 D :超额领料 |
| 60 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 61 | fprojecttaskid | fprojecttaskid | int8 | 64 |  | √ | 0 |  |
| 62 | fmaintrade | 主行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 63 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 64 | ftransmittime | 下达时间 | timestamp | 0 |  |  | null | 下达时间 |
| 65 | fisrecheck | 是否复检 | bpchar | 1 |  | √ | '0' | 是否复检 |
| 66 | fmodifystatustime | 状态更新时间 | timestamp | 0 |  |  | null | 状态更新时间 |
| 67 | fdefectreasonid | 缺陷原因 | int8 | 64 |  | √ | 0 | 缺陷原因 fmm_defectreason |
| 68 | fworkhourunitid | 工时单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 69 | fisassist | 请求协助 | bpchar | 1 |  | √ | '0' | 请求协助 |
| 70 | fproducedept | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 71 | fproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 72 | fplanstatus | 计划状态 | varchar | 50 |  | √ | ' ' | 计划状态,枚举: A :计划 B :计划确认 C :下达 |
| 73 | fproductmodel | 产品型号 | int8 | 64 |  | √ | 0 | 工卡维护 mpdm_workcards |
| 74 | fplanhours | 计划消耗工时 | numeric | 23 | 10 | √ | 0 | 计划消耗工时 |
| 75 | fsourcebillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 76 | fassisthours | 协助填写预估工时 | numeric | 23 | 10 | √ | 0 | 协助填写预估工时 |
| 77 | fplanbaseqty | 计划基本数量 | numeric | 23 | 10 | √ | 0 | 计划基本数量 |
| 78 | fplanendtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 79 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 80 | fresourcestatus | 资源就绪状态 | varchar | 50 |  | √ | ' ' | 资源就绪状态,枚举: A :未就绪 B :预计就绪 C :实际就绪 |
| 81 | fendworktime | 完工时间 | timestamp | 0 |  |  | null | 完工时间 |
| 82 | fauxptyqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_mroorderentry |  | fentryid |
| 2 | idx_mroorderentry_fcfgcodeid |  | fconfiguredcodeid |
| 3 | idx_mroorderentry_ftrackid |  | ftracknumberid |
| 4 | idx_pom_mroorderentry_fsrcseq |  | fsourceentryseq |
| 5 | idx_mroorderentry_fk |  | fid |

---

## WBS-多选基础资料表 t_pom_mulwbs

- **表名称：** WBS-多选基础资料表
- **表名：** t_pom_mulwbs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | WBS pmts_wbs |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pom_mulwbs |  | fpkid |
| 2 | idx_pom_mulwbs_fk |  | fentryid |

---

## 检修工单-反写记录表 t_pom_mroorder_wb

- **表名称：** 检修工单-反写记录表
- **表名：** t_pom_mroorder_wb

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
| 1 | pk_pom_mroorder_wb |  | fentryid |
| 2 | idx_pom_mroorder_wb_fk |  | fid |

---

## 类型标识-多选基础资料表 t_pom_multypeid

- **表名称：** 类型标识-多选基础资料表
- **表名：** t_pom_multypeid

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | 类型标识 mpdm_typeidentity |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_multypeid_fk |  | fentryid |
| 2 | pk_t_pom_multypeid |  | fpkid |
