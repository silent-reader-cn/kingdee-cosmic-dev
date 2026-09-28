# 显示方案-psw_displayscheme

## 单据体-子表 t_psw_capacityplandetail

- **表名称：** 单据体-子表
- **表名：** t_psw_capacityplandetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwarnthreshold | 红色阈值（警告） | varchar | 50 |  | √ | ' ' | 红色阈值（警告） |
| 3 | fforewarnto |  | numeric | 23 | 10 | √ | 0 |  |
| 4 | fthresholdtype | 对象\阈值类型 | varchar | 50 |  | √ | ' ' | 对象\阈值类型,枚举: 0 :产能利用率% 1 :日剩余产能（小时） 2 :累计剩余产能（小时） |
| 5 | fforewarnbetween |  | numeric | 23 | 10 | √ | 0 |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fsymbol | 黄色阈值（预警） | varchar | 10 |  | √ | ' ' | 黄色阈值（预警） |
| 8 | fnormalthreshold | 绿色阈值（正常） | varchar | 50 |  | √ | ' ' | 绿色阈值（正常） |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_psw_capacityplandetail |  | fentryid |
| 2 | idx_t_psw_cpdetail |  | fid |

---

## 显示方案-主表 t_psw_displayscheme

- **表名称：** 显示方案-主表
- **表名：** t_psw_displayscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fshowana | 平衡后自动应用生产调整建议 | bpchar | 1 |  | √ | ' ' | 平衡后自动应用生产调整建议 |
| 4 | fhidenonworkday | 仅显示工作日 | bpchar | 1 |  | √ | '0' | 仅显示工作日 |
| 5 | fstockoutmaterial | 仅显示缺货物料 | bpchar | 1 |  | √ | ' ' | 仅显示缺货物料 |
| 6 | fcacdaycnt | 可用性检查天数 | int8 | 64 |  | √ | 0 | 可用性检查天数 |
| 7 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | fgeneratelog | 生成日志 | bpchar | 1 |  | √ | '0' | 生成日志 |
| 9 | fcacexpandlevel | 默认展开层数 | int8 | 64 |  | √ | 0 | 默认展开层数 |
| 10 | flevelingstrategy | 排程策略 | bpchar | 1 |  | √ | '0' | 排程策略,枚举: 0 :客户需求优先 1 :产能瓶颈优先 |
| 11 | fhasplanmaterial | 仅显示有生产线计划的物料 | bpchar | 1 |  | √ | ' ' | 仅显示有生产线计划的物料 |
| 12 | fdefaultscheme | 默认方案 | bpchar | 1 |  | √ | ' ' | 默认方案,枚举: 0 :是 1 :否 |
| 13 | fautobucket | 自动排程 | bpchar | 1 |  | √ | ' ' | 自动排程 |
| 14 | fratedqty | 额定日产量 | bpchar | 1 |  | √ | '0' | 额定日产量 |
| 15 | fschemename | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 16 | ffixedtermplan | 计划固定期（天） | int4 | 32 |  | √ | 0 | 计划固定期（天） |
| 17 | fislevelbyshift | 班次级排程 | bpchar | 1 |  | √ | '1' | 班次级排程 |
| 18 | fcacdisplayctrl | 显示字段控制 | varchar | 50 |  | √ | ' ' | 显示字段控制,枚举: 0 :关键件 1 :替代件 2 :即时库存 3 :安全库存 4 :基本单位 5 :物料属性 |
| 19 | fdisplaycontrol | 显示控制 | varchar | 50 |  | √ | ' ' | 显示控制,枚举: 0 :日计划产能 1 :累计计划产能 2 :产能利用率% 3 :日产能负载 4 :累计产能负载 5 :日生产数量 6 :累计生产数量 7 :日剩余产能 8 :累计剩余产能 |
| 20 | fmaterialinfoconfig | 物料信息 | varchar | 50 |  | √ | ' ' | 物料信息,枚举: 0 :物料编码 1 :物料名称 2 :规格型号 3 :物料版本 4 :辅助属性 |
| 21 | fproductionorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fday | 按日排程（天） | int8 | 64 |  | √ | 0 | 按日排程（天） |
| 23 | fbucketdatemodel | 排程时段模式 | varchar | 50 |  | √ | ' ' | 排程时段模式,枚举: 0 :按日排程 1 :按周排程 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_psw_displayscheme |  | fid |
| 2 | idx_t_psw_ds_union |  | fschemename,fproductionorgid,fcreator |
