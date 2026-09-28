# 安全库存记录-invp_safestock_record

## 安全库存记录-多语言表 t_invp_ssrecord_l

- **表名称：** 安全库存记录-多语言表
- **表名：** t_invp_ssrecord_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_ssrecord_l |  | fid,flocaleid |
| 2 | pk_t_invp_ssrecord_l |  | fpkid |

---

## 安全库存记录-主表 t_invp_ssrecord

- **表名称：** 安全库存记录-主表
- **表名：** t_invp_ssrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fsafestockdays | 安全库存天数 | numeric | 23 | 4 | √ | 0 | 安全库存天数 |
| 8 | fmaterialgroupid | 物料分类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 9 | fconsumeperday | 日均消耗量 | numeric | 23 | 4 | √ | 0 | 日均消耗量 |
| 10 | fschemeid | 统计方案 | int8 | 64 |  | √ | 0 | 安全库存统计方案 invp_safestock_scheme |
| 11 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fsafestock | 安全库存 | numeric | 23 | 2 | √ | 0 | 安全库存 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fgroupstandardid | 物料分类标准 | int8 | 64 |  | √ | 0 | 物料分类标准 bd_materialgroupstandard |
| 20 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 21 | fbaseunitid | fbaseunitid | int8 | 64 |  | √ | 0 |  |
| 22 | fkeycol | KEYCOL | varchar | 50 |  | √ | ' ' | KEYCOL |
| 23 | fdimension | 库存水位维度 | int8 | 64 |  | √ | 0 | 库存水位维度 msplan_plan_dimension |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_invp_ssrecord_org |  | fbizorgid |
| 2 | pk_t_invp_ssrecord |  | fid |
