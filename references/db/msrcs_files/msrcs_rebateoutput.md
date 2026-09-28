# 计算输出规则-msrcs_rebateoutput

## 计算输出规则-多语言表 t_msrcs_rebateoutput_l

- **表名称：** 计算输出规则-多语言表
- **表名：** t_msrcs_rebateoutput_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msrcs_rebateoutput_l |  | fpkid |
| 2 | idx_msrcs_rebateoutputl_flid |  | fid,flocaleid |

---

## 计算输出规则-主表 t_msrcs_rebateoutput

- **表名称：** 计算输出规则-主表
- **表名：** t_msrcs_rebateoutput

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ffilterscheme | 自定义过滤条件 | varchar | 2000 |  | √ | ' ' | 自定义过滤条件 |
| 6 | fcalresultid | 计算结果 | varchar | 40 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 7 | fnodatamodel | 无结果输出时处理 | bpchar | 1 |  | √ | 'A' | 无结果输出时处理,枚举: A :不生成目标对象 B :生成目标对象 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fpolicytargetid | 政策对象 | varchar | 40 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | foutputid | 输出目标 | varchar | 40 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | frebatemodelid | 返利计算模型 | varchar | 40 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | frebateschemaid | 返利计算方案 | int8 | 64 |  | √ | 0 | 返利计算方案 msrcs_rebateschema |
| 17 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | fissyspreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msrcs_rebateoutput |  | fid |
| 2 | idx_msrcs_rebateoutput_num |  | fnumber |

---

## 属性单据体-子表 t_msrcs_rebateoutput_be

- **表名称：** 属性单据体-子表
- **表名：** t_msrcs_rebateoutput_be

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fupdatetype | 更新策略 | bpchar | 1 |  | √ | ' ' | 更新策略,枚举: A :新增修改全更新 B :仅新增更新 |
| 3 | ffieldformula | 计算公式 | varchar | 2000 |  | √ | ' ' | 计算公式 |
| 4 | fhandtype | 控制方式 | bpchar | 1 |  | √ | ' ' | 控制方式,枚举: A :单头主键 B :分录主键 C :行数据重复时合并数据 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsourcefieldtype | 源字段来源 | bpchar | 1 |  | √ | ' ' | 源字段来源,枚举: A :返利模型 B :政策对象 C :输出目标 D :计算结果 |
| 7 | fvaluetype | 取值方式 | bpchar | 1 |  | √ | ' ' | 取值方式,枚举: 0 :源字段 1 :计算公式 2 :按条件取值 3 :常量 |
| 8 | fsname | 源字段名称 | varchar | 80 |  | √ | ' ' | 源字段名称 |
| 9 | fconditionformula | 条件取值计算公式 | varchar | 255 |  | √ | ' ' | 条件取值计算公式 |
| 10 | ffieldformuladesc | 计算公式 | varchar | 80 |  | √ | ' ' | 计算公式 |
| 11 | fsid | 源字段标识 | varchar | 80 |  | √ | ' ' | 源字段标识 |
| 12 | ftid | 目标字段标识 | varchar | 80 |  | √ | ' ' | 目标字段标识 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | ftname | 目标字段名称 | varchar | 80 |  | √ | ' ' | 目标字段名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msrcs_rebateoutput_be |  | fentryid |
| 2 | idx_msrcs_rebateoutputbe_fid |  | fid |
