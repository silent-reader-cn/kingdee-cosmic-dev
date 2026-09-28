# 模板配置-rdem_template

## 模板配置-多语言表 t_rdem_template_l

- **表名称：** 模板配置-多语言表
- **表名：** t_rdem_template_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 报表名称 | varchar | 155 |  | √ | ' ' | 报表名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_template_l |  | fpkid |
| 2 | idx_rdem_template_l_0 |  | fid,flocaleid |

---

## 模板配置-主表 t_rdem_template

- **表名称：** 模板配置-主表
- **表名：** t_rdem_template

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 报表名称 | varchar | 100 |  | √ | ' ' | 报表名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodelid | 体系 | int8 | 64 |  | √ | 0 | [体系管理 rdem_model](../rdem_files/rdem_model.md) |
| 6 | fconditionjson | 配置条件 | varchar | 2000 |  | √ | ' ' | 配置条件 |
| 7 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fenddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fgeneral | 通用 | bpchar | 1 |  | √ | '0' | 通用 |
| 12 | ftype | 报表类型 | varchar | 36 |  | √ | ' ' | [模板类型 tctb_template_type](../tctb_files/tctb_template_type.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcontent_tag | 模板内容_详情 | text | 0 |  |  | null | 模板内容_详情 |
| 16 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 报表编码 | varchar | 30 |  | √ | ' ' | 报表编码 |
| 19 | fcontent | 模板内容 | varchar | 255 |  | √ | ' ' | 模板内容 |
| 20 | ffiltercondition | 配置条件 | varchar | 2000 |  | √ | ' ' | 配置条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_template |  | fid |
| 2 | idx_rdem_template_m0 |  | fmasterid |

---

## 单据体-子表 t_rdem_temp_rep_relation

- **表名称：** 单据体-子表
- **表名：** t_rdem_temp_rep_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freportitemid | 报表项 | int8 | 64 |  | √ | 0 | [报表项 rdem_report_item](../rdem_files/rdem_report_item.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | frowcol | 行列维组合标识 | varchar | 128 |  | √ | ' ' | 行列维组合标识 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_temp_rep_relation_fk |  | fid |
| 2 | pk_rdem_temp_rep_relation |  | fentryid |
