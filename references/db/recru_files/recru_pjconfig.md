# 人岗匹配配置-recru_pjconfig

## 人岗匹配配置-多语言表 t_recru_pjmatchconfig_l

- **表名称：** 人岗匹配配置-多语言表
- **表名：** t_recru_pjmatchconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_pjmatchconfig_l |  | fid,flocaleid |
| 2 | pk_recru_pjmatchconfig_l |  | fpkid |

---

## 匹配度标签显示规则-子表 t_recru_configruleentity

- **表名称：** 匹配度标签显示规则-子表
- **表名：** t_recru_configruleentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fshow | 是否在列表展示 | varchar | 2 |  | √ | ' ' | 是否在列表展示,枚举: 1 :是 0 :否 |
| 3 | fconfigrulelow | 匹配度最低值（闭区间） | numeric | 23 | 10 | √ | 0 | 匹配度最低值（闭区间） |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fmatchname | 匹配度标签名称 | varchar | 200 |  | √ | ' ' | 匹配度标签名称 |
| 7 | fmatchnamekey | 匹配标签标识 | varchar | 50 |  | √ | ' ' | 匹配标签标识 |
| 8 | fconfigrulehigh | 匹配度最高值（开区间） | numeric | 23 | 10 | √ | 0 | 匹配度最高值（开区间） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_configruleentity_fid |  | fid |
| 2 | pk_recru_configruleentity |  | fentryid |

---

## 匹配度标签显示规则-多语言表 t_recru_configruleentity_l

- **表名称：** 匹配度标签显示规则-多语言表
- **表名：** t_recru_configruleentity_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fmatchname | 匹配度标签名称 | varchar | 200 |  | √ | ' ' | 匹配度标签名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_configruleentity_l |  | fpkid |
| 2 | idx_recru_configruleentity_l |  | fentryid,flocaleid |

---

## 向量匹配维度权重配置-子表 t_recru_dimensionweight

- **表名称：** 向量匹配维度权重配置-子表
- **表名：** t_recru_dimensionweight

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fweight | 权重（%） | int4 | 32 |  | √ | 0 | 权重（%） |
| 3 | fseq | 分录行号 | varchar | 50 |  | √ | ' ' | 分录行号 |
| 4 | fdimensionkey | 维度标识 | varchar | 50 |  | √ | ' ' | 维度标识 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fdimension | 维度 | varchar | 200 |  | √ | ' ' | 维度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_dimensionweight_fid |  | fid |
| 2 | pk_recru_dimensionweight |  | fentryid |

---

## 工作经验配置-子表 t_recru_expconfigentity

- **表名称：** 工作经验配置-子表
- **表名：** t_recru_expconfigentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexphigh | 范围最高值（开区间） | numeric | 23 | 10 | √ | 0 | 范围最高值（开区间） |
| 3 | fexppercent | 占比（%） | int4 | 32 |  | √ | 0 | 占比（%） |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fexplow | 范围最低值（闭区间） | numeric | 23 | 10 | √ | 0 | 范围最低值（闭区间） |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_expconfigentity |  | fentryid |
| 2 | idx_recru_expconfigentity_fid |  | fid |

---

## 人岗匹配配置-主表 t_recru_pjmatchconfig

- **表名称：** 人岗匹配配置-主表
- **表名：** t_recru_pjmatchconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freranker | 是否启用重排序 | bpchar | 1 |  | √ | '0' | 是否启用重排序 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fshowpositionnum | 猜你合适列表推荐职位数量 | int4 | 32 |  | √ | 0 | 猜你合适列表推荐职位数量 |
| 6 | fshowpersonnum | 推荐候选人列表数量 | int4 | 32 |  | √ | 0 | 推荐候选人列表数量 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | findex | 排序号 | int4 | 32 |  | √ | 0 | 排序号 |
| 9 | frerankermodel | 重排模型编码 | varchar | 100 |  | √ | ' ' | 重排模型编码 |
| 10 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 11 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | ftopk | topk | int4 | 32 |  | √ | 0 | topk |
| 15 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | freranksimilarity | 重排返回相似度最低值 | numeric | 23 | 10 | √ | 0 | 重排返回相似度最低值 |
| 19 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 21 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 22 | fsimilarity | 初排返回相似度最低值 | numeric | 23 | 10 | √ | 0 | 初排返回相似度最低值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_pjmatchconfig_num |  | fnumber |
| 2 | pk_recru_pjmatchconfig |  | fid |

---

## 向量匹配维度权重配置-多语言表 t_recru_dimensionweight_l

- **表名称：** 向量匹配维度权重配置-多语言表
- **表名：** t_recru_dimensionweight_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fdimension | 维度 | varchar | 200 |  | √ | ' ' | 维度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_dimensionweight_l |  | fentryid,flocaleid |
| 2 | pk_recru_dimensionweight_l |  | fpkid |
