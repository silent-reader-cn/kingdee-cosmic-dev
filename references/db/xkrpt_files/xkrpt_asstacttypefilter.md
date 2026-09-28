# 核算维度过滤方案-xkrpt_asstacttypefilter

## 核算维度过滤方案-多语言表 t_xkrpt_asstacttypefilter_l

- **表名称：** 核算维度过滤方案-多语言表
- **表名：** t_xkrpt_asstacttypefilter_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmulirptdimname | 编制维度值 | varchar | 570 |  | √ | ' ' | 编制维度值 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fmuliattributename | 属性字段 | varchar | 570 |  | √ | ' ' | 属性字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_asstacttypefilter_l |  | fpkid |
| 2 | idx_xkrpt_asstfilter_l |  | fid,flocaleid |

---

## 核算维度过滤方案-主表 t_xkrpt_asstacttypefilter

- **表名称：** 核算维度过滤方案-主表
- **表名：** t_xkrpt_asstacttypefilter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 5 | fdimmapping | 预算维度映射方案 | int8 | 64 |  | √ | 0 | [预算维度映射 xkbm_dimmapping](../xkbm_files/xkbm_dimmapping.md) |
| 6 | ffiltertype | 方案类型 | varchar | 10 |  | √ | ' ' | 方案类型,枚举: 0 :自定义匹配 1 :编码匹配 2 :名称匹配 3 :维度与属性维度 4 :维度与多层级维度 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fconditionjson | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 9 | fconditionjson_tag | 过滤条件_详情 | varchar | 2000 |  | √ | ' ' | 过滤条件_详情 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fmuliattributename | 属性字段 | varchar | 570 |  | √ | ' ' | 属性字段 |
| 12 | fmulirptdimname | 编制维度值 | varchar | 570 |  | √ | ' ' | 编制维度值 |
| 13 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fattributekey | 属性字段keu | varchar | 500 |  | √ | ' ' | 属性字段keu |
| 17 | frptdimension | 编制维度 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 18 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 20 | frptdimid | 编制维度值id | varchar | 50 |  | √ | ' ' | 编制维度值id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_asstfilter_gropid |  | fgroupid |
| 2 | pk_xkrpt_asstacttypefilter |  | fid |
