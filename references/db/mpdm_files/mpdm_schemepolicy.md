# 应用隐私政策-mpdm_schemepolicy

## 应用隐私政策-多语言表 t_mpdm_schemepolicy_l

- **表名称：** 应用隐私政策-多语言表
- **表名：** t_mpdm_schemepolicy_l

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
| 1 | pk_mpdm_schemepolicy_l |  | fpkid |
| 2 | idx_mpdm_schemepol_l_flid |  | fid,flocaleid |

---

## 应用隐私政策-主表 t_mpdm_schemepolicy

- **表名称：** 应用隐私政策-主表
- **表名：** t_mpdm_schemepolicy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freleasetime | 发布时间 | timestamp | 0 |  |  | null | 发布时间 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fpolicypaperwork | 隐私政策文案 | varchar | 255 |  | √ | ' ' | 隐私政策文案 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | freleasevserion | 发布版本 | varchar | 255 |  | √ | ' ' | 发布版本 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fpolicypaperwork_tag | 隐私政策文案_详情 | text | 0 |  |  | null | 隐私政策文案_详情 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 15 | fhpschemeid | 首页方案 | int8 | 64 |  | √ | 0 | 移动首页方案 mpdm_hpschemeconfig |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_schemepolicy |  | fid |
| 2 | idx_mpdm_schemepolicy_number |  | fnumber |
