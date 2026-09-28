# 规则定义-bos_devp_rule

## 规则定义-多语言表 t_dm_rule_l

- **表名称：** 规则定义-多语言表
- **表名：** t_dm_rule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dm_rule_l_fk |  | fid |
| 2 | pk_dm_rule_l |  | fpkid |

---

## 规则定义-主表 t_dm_rule

- **表名称：** 规则定义-主表
- **表名：** t_dm_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fclass | 实现类 | varchar | 500 |  |  | null | 实现类 |
| 3 | ffieldchanged | 值更新 | bpchar | 1 |  | √ | '0' | 值更新 |
| 4 | fisv | 开发商标识 | varchar | 10 |  | √ | ' ' | 开发商标识 |
| 5 | fformrule | 表单 | bpchar | 1 |  | √ | '0' | 表单 |
| 6 | ftype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: formmeta :界面规则 entitymeta :业务规则 |
| 7 | fadd | 创建 | bpchar | 1 |  | √ | '0' | 创建 |
| 8 | flist | 列表控件 | bpchar | 1 |  | √ | '0' | 列表控件 |
| 9 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 11 | fload | 加载 | bpchar | 1 |  | √ | '0' | 加载 |
| 12 | freport | 报表控件 | bpchar | 1 |  | √ | '0' | 报表控件 |
| 13 | fcard | 卡片控件 | bpchar | 1 |  | √ | '0' | 卡片控件 |
| 14 | fformid | 定义参数 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_dm_rule_number |  | fnumber |
| 2 | pk_dm_rule |  | fid |
