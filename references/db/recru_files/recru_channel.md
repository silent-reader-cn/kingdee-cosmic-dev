# 渠道管理-recru_channel

## 渠道管理-多语言表 t_recru_channel_l

- **表名称：** 渠道管理-多语言表
- **表名：** t_recru_channel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 渠道名称 | varchar | 50 |  | √ | ' ' | 渠道名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_channel_l |  | fpkid |
| 2 | idx_recru_channel_l_fid |  | fid,flocaleid |

---

## 渠道管理-主表 t_recru_channel

- **表名称：** 渠道管理-主表
- **表名：** t_recru_channel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 渠道名称 | varchar | 50 |  | √ | ' ' | 渠道名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | findex | 排序号 | int4 | 32 |  | √ | 0 | 排序号 |
| 6 | fmodelnumber | 模型编码 | varchar | 100 |  | √ | ' ' | 模型编码 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |
| 9 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ftype | 类型 | varchar | 2 |  | √ | ' ' | 类型,枚举: 1 :内部招聘 2 :社会招聘 |
| 13 | fcontent_tag | 内容_详情 | text | 0 |  |  | null | 内容_详情 |
| 14 | fscene | 适用场景 | varchar | 200 |  | √ | ' ' | 适用场景,枚举: |
| 15 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | furl | 渠道地址 | varchar | 50 |  | √ | ' ' | 渠道地址 |
| 17 | fchanneltype | 渠道类型 | varchar | 2 |  | √ | ' ' | 渠道类型,枚举: A :金蝶云星瀚·内部招聘 B :金蝶云星瀚·外部人才库 C :智联招聘 D :猎聘 E :Boss |
| 18 | fnumber | 渠道编码 | varchar | 30 |  | √ | ' ' | 渠道编码 |
| 19 | fdownloadcount | 简历下载数量 | int4 | 32 |  | √ | 0 | 简历下载数量 |
| 20 | futility | 适用功能 | varchar | 200 |  | √ | ' ' | 适用功能,枚举: |
| 21 | fcontent | 内容 | varchar | 255 |  | √ | ' ' | 内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_channel |  | fid |
| 2 | idx_recru_channel_number |  | fnumber |
