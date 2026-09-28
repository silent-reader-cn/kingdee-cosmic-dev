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
| 2 | fschemename | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fshowana | 平衡后自动应用生产调整建议 | bpchar | 1 |  | √ | ' ' | 平衡后自动应用生产调整建议 |
| 5 | fstockoutmaterial | 仅显示缺货物料 | bpchar | 1 |  | √ | ' ' | 仅显示缺货物料 |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fdisplaycontrol | 显示控制 | varchar | 50 |  | √ | ' ' | 显示控制,枚举: 0 :日计划产能 1 :累计计划产能 2 :产能利用率% 3 :日产能负载 4 :累计产能负载 5 :日生产数量 6 :累计生产数量 7 :日剩余产能 8 :累计剩余产能 |
| 8 | fmaterialinfoconfig | 物料信息 | varchar | 50 |  | √ | ' ' | 物料信息,枚举: 0 :物料编码 1 :物料名称 2 :规格型号 3 :物料版本 4 :辅助属性 |
| 9 | fproductionorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fhasplanmaterial | 仅显示有生产线计划的物料 | bpchar | 1 |  | √ | ' ' | 仅显示有生产线计划的物料 |
| 11 | fdefaultscheme | 默认方案 | bpchar | 1 |  | √ | ' ' | 默认方案,枚举: 0 :是 1 :否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_psw_displayscheme |  | fid |
| 2 | idx_t_psw_ds_union |  | fschemename,fproductionorgid,fcreator |
