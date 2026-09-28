# 国际贸易关务集成日志-gtm_slintegratelog

## 国际贸易关务集成日志-主表 t_gtm_slintegratelog

- **表名称：** 国际贸易关务集成日志-主表
- **表名：** t_gtm_slintegratelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcaller | 调用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | finparameter_tag | 请求参数_详情 | text | 0 |  |  | null | 请求参数_详情 |
| 7 | fresult | 返回结果 | varchar | 255 |  | √ | ' ' | 返回结果 |
| 8 | fthirdbillnumber | 第三方单据编号 | varchar | 255 |  | √ | ' ' | 第三方单据编号 |
| 9 | fcalldatetime | 调用开始时间 | timestamp | 0 |  |  | null | 调用开始时间 |
| 10 | fthirdcompany | 第三方集成服务商 | varchar | 5 |  | √ | ' ' | 第三方集成服务商,枚举: 0 :空 1 :数联 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fresult_tag | 返回结果_详情 | text | 0 |  |  | null | 返回结果_详情 |
| 13 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | frequesturl | 请求URL | varchar | 2000 |  | √ | ' ' | 请求URL |
| 17 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fcallenddatetime | 调用结束时间 | timestamp | 0 |  |  | null | 调用结束时间 |
| 19 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 20 | finparameter | 请求参数 | varchar | 255 |  | √ | ' ' | 请求参数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_slintegratelog |  | fid |

---

## 国际贸易关务集成日志-多语言表 t_gtm_slintegratelog_l

- **表名称：** 国际贸易关务集成日志-多语言表
- **表名：** t_gtm_slintegratelog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gtm_slintegratelog_l_id |  | fid,flocaleid |
| 2 | pk_gtm_slintegratelog_l |  | fpkid |
