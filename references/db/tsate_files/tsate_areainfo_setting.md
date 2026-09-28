# 税企直连行政区化配置-tsate_areainfo_setting

## 税企直连行政区化配置-主表 t_tsate_areainfo_setting

- **表名称：** 税企直连行政区化配置-主表
- **表名：** t_tsate_areainfo_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 区划名称 | varchar | 100 |  | √ | ' ' | 区划名称 |
| 3 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fbaseareanumber | 基础运维区划编码 | varchar | 80 |  | √ | ' ' | 基础运维区划编码 |
| 9 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fqxynumber | 企享云区划编码 | varchar | 50 |  | √ | ' ' | 企享云区划编码 |
| 11 | fnumber | 公共编码 | varchar | 30 |  | √ | ' ' | 公共编码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_areaset_qxyno |  | fqxynumber |
| 2 | pk_tsate_areainfo_setting |  | fid |

---

## 税企直连行政区化配置-多语言表 t_tsate_areainfo_setting_l

- **表名称：** 税企直连行政区化配置-多语言表
- **表名：** t_tsate_areainfo_setting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 区划名称 | varchar | 100 |  | √ | ' ' | 区划名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_areainfo_setting_l_0 |  | fid,flocaleid |
| 2 | pk_tsate_areainfo_setting_l |  | fpkid |
