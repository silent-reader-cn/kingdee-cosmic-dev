# 显示方案-arm_displayscheme

## 显示方案-主表 t_arm_displayscheme

- **表名称：** 显示方案-主表
- **表名：** t_arm_displayscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fchartdisplay | 显示设置 | varchar | 255 |  | √ | ' ' | 显示设置,枚举: plancompleterateflex :计划完成率 qualificationrateflex :合格率 invstatusflex :入库情况 qualifiedanalysisflex :良品分析 productionorderflex :重复生产工单 reportrecordflex :汇报记录 linedemandflex :生产线需求 planorderflex :计划订单 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fuserid | 用户id | int8 | 64 |  | √ | 0 | 用户id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_arm_displayscheme |  | fid |
| 2 | idx_arm_displayscheme_m0 |  | fuserid |

---

## 单据体-子表 t_arm_capacityplandetail

- **表名称：** 单据体-子表
- **表名：** t_arm_capacityplandetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcolorsettings | 颜色设置 | varchar | 50 |  | √ | ' ' | 颜色设置,枚举: 0 :计划完成率% 1 :合格率% |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fwarnthreshold | 红色阈值（警告） | varchar | 50 |  | √ | ' ' | 红色阈值（警告） |
| 4 | fforewarnto |  | numeric | 23 | 3 | √ | 0 |  |
| 5 | fforewarnbetween |  | numeric | 23 | 3 | √ | 0 |  |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsymbol | 黄色阈值（预警） | varchar | 50 |  | √ | ' ' | 黄色阈值（预警） |
| 8 | fnormalthreshold | 绿色阈值（正常） | varchar | 50 |  | √ | ' ' | 绿色阈值（正常） |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_arm_capacityplandetail |  | fentryid |
| 2 | idx_arm_capacityplandetail_fk |  | fid |
