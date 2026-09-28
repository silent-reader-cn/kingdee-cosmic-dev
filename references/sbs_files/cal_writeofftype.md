# 核销类别（旧）-cal_writeofftype

## 核销类别（旧）-主表 t_sbs_writeofftype

- **表名称：** 核销类别（旧）-主表
- **表名：** t_sbs_writeofftype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fissys | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 8 | fmasterbillid | 主方单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 9 | fenable | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 11 | fasstbillid | 辅方单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sbs_writeofftype_pkey |  | fid |
| 2 | idx_sbs_writeofftype_fno |  | fnumber |

---

## 核销类别（旧）-多语言表 t_sbs_writeofftype_l

- **表名称：** 核销类别（旧）-多语言表
- **表名：** t_sbs_writeofftype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sbs_writeofftype_l_pkey |  | fpkid |
| 2 | idx_sbs_writeofftype_l |  | fid |
