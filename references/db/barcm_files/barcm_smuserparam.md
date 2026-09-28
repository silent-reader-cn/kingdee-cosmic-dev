# 条码扫描模型用户参数表-barcm_smuserparam

## 条码扫描模型用户参数表-主表 t_barcm_smuparam

- **表名称：** 条码扫描模型用户参数表-主表
- **表名：** t_barcm_smuparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | ftwbcassfield | 调拨仓位条码赋值字段 | bpchar | 1 |  | √ | ' ' | 调拨仓位条码赋值字段,枚举: A :入库 B :出库 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbarcodenumber | 条码段 | varchar | 2 |  | √ | '0' | 条码段,枚举: 1 :1 2 :2 |
| 7 | fpdaeditmode | PDA录单模式 | bpchar | 1 |  | √ | 'B' | PDA录单模式,枚举: A :连续 B :单条 |
| 8 | fnoboxnumpack | 无箱号包装 | bpchar | 1 |  | √ | '0' | 无箱号包装 |
| 9 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fpdascanmode | 连续扫描方式 | bpchar | 1 |  | √ | 'A' | 连续扫描方式,枚举: A :自动接收上一条 B :自动接收当前 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsbilldatecondition | 源单日期过滤条件 | bpchar | 1 |  | √ | ' ' | 源单日期过滤条件,枚举: A :全部 B :今天 C :本月 D :今年 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 18 | fnobncontainersize | 无箱号包装容器容量 | int4 | 32 |  | √ | 1 | 无箱号包装容器容量 |
| 19 | fscanmodelid | 条码扫描模型 | int8 | 64 |  | √ | 0 | [条码扫描模型 barcm_scanningmodel](../barcm_files/barcm_scanningmodel.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_smup_number |  | fnumber |
| 2 | pk_barcm_smuparam |  | fid |

---

## 条码扫描模型用户参数表-多语言表 t_barcm_smuparam_l

- **表名称：** 条码扫描模型用户参数表-多语言表
- **表名：** t_barcm_smuparam_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_smuparam_l |  | fpkid |
| 2 | idx_barcm_smup_l_fidfld |  | fid,flocaleid |
