# 批号唯一值范围配置-msmod_lotmfunirangeconf

## 批号唯一值范围配置-主表 t_msmod_lotmfunirangeconf

- **表名称：** 批号唯一值范围配置-主表
- **表名：** t_msmod_lotmfunirangeconf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 50 |  | √ | '1' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fintroduce | 说明 | varchar | 200 |  | √ | '修改说明：生成批号主档后，为了避免冲突，唯一值范围只能缩小，不允许扩大' | 说明 |
| 6 | fdescription | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fenable | 使用状态 | varchar | 50 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 13 | funiquerange | 唯一值范围 | bpchar | 1 |  | √ | ' ' | 唯一值范围,枚举: 1 :全局 2 :物料 3 :组织 4 :组织+物料 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_lotmfunircfg_number |  | fnumber |
| 2 | pk_t_msmod_lotmfunirangeconf |  | fid |

---

## 批号唯一值范围配置-多语言表 t_msmod_lotmfunirangeconf_l

- **表名称：** 批号唯一值范围配置-多语言表
- **表名：** t_msmod_lotmfunirangeconf_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_lotmfunicfg_l_flid |  | fid,flocaleid |
| 2 | pk_t_msmod_lotmfunirangeconf_l |  | fpkid |
