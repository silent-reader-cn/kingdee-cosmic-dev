# 自定义数据源适用取数规则-tctb_datasource_peek_rule

## 自定义数据源适用取数规则-多语言表 t_tctb_datasource_pekrule_l

- **表名称：** 自定义数据源适用取数规则-多语言表
- **表名：** t_tctb_datasource_pekrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_datasource_pekrule_l |  | fid,flocaleid |
| 2 | pk_tctb_datasource_pekrule_l |  | fpkid |

---

## 自定义数据源适用取数规则-主表 t_tctb_datasource_pekrule

- **表名称：** 自定义数据源适用取数规则-主表
- **表名：** t_tctb_datasource_pekrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 5 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 6 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 7 | fgroupfield | 规则分类 | int8 | 64 |  | √ | 0 | 自定义数据源税种适用规则 tctb_datasouce_rule_tax |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_datasource_pekrule |  | fnumber,fgroupfield |
| 2 | pk_tctb_datasource_pekrule |  | fid |
