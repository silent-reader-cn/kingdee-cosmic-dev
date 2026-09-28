# 标准工时维护-scax_standardhour

## 标准工时维护-主表 t_scax_standardhour

- **表名称：** 标准工时维护-主表
- **表名：** t_scax_standardhour

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmaterialgroupstandard | 物料分类标准 | int8 | 64 |  | √ | 0 | [物料分类标准 bd_materialgroupstandard](../basedata_files/bd_materialgroupstandard.md) |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcosttype | 标准成本方案 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 11 | faccording | 设置依据 | bpchar | 1 |  | √ | ' ' | 设置依据,枚举: 1 :按物料分类标准设置 2 :按物料编码设置 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scax_standardhour |  | fid |
| 2 | idx_scax_standardhour |  | fbillno |

---

## 标准工时维护-多语言表 t_scax_standardhour_l

- **表名称：** 标准工时维护-多语言表
- **表名：** t_scax_standardhour_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scax_standardhour_l |  | fpkid |
| 2 | idx_t_scax_standardhour_l |  | fid,flocaleid |

---

## 物料信息-子表 t_scax_standardhourentry

- **表名称：** 物料信息-子表
- **表名：** t_scax_standardhourentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialgroup | 物料分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 3 | fbaseunitnum | 基准单位分子 | numeric | 23 | 10 | √ | 0 | 基准单位分子 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdatasrc | 数据来源 | varchar | 100 |  | √ | 'manual' | 数据来源,枚举: manual :手工新增 mfthour :物料生产工时 |
| 6 | fmaterialcommon | 物料组织公共信息 | int8 | 64 |  | √ | 0 | [物料组织公共信息 bd_materialcommon](../basedata_files/bd_materialcommon.md) |
| 7 | fbaseunit | 基准工时单位 | varchar | 30 |  | √ | ' ' | 基准工时单位,枚举: 1 :时 2 :分 3 :秒 |
| 8 | flaborreadyhour | 准备人工 | numeric | 23 | 10 | √ | 0 | 准备人工 |
| 9 | flaborworkhour | 人员操作工时 | numeric | 23 | 10 | √ | 0 | 人员操作工时 |
| 10 | fmachinereadyhour | 准备机器 | numeric | 23 | 10 | √ | 0 | 准备机器 |
| 11 | fmachineworkhour | 机器操作工时 | numeric | 23 | 10 | √ | 0 | 机器操作工时 |
| 12 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 13 | ffactor | 工时基数 | int4 | 32 |  | √ | 0 | 工时基数 |
| 14 | fbaseunitden | 基准单位分母 | numeric | 23 | 10 | √ | 0 | 基准单位分母 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | funit | 工时单位 | bpchar | 1 |  | √ | ' ' | 工时单位,枚举: 1 :时 2 :分 3 :秒 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scax_standardhourentry |  | fid |
| 2 | pk_scax_standardhourentry |  | fentryid |
