# 促销类型校验配置-ocdpm_promodeploy

## 促销策略-多选基础资料表 t_ocdpm_deploystrategyn

- **表名称：** 促销策略-多选基础资料表
- **表名：** t_ocdpm_deploystrategyn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [渠道促销策略 ocdpm_promotionstrategy](../ocdpm_files/ocdpm_promotionstrategy.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_deploystrategyn |  | fpkid |
| 2 | idx_ocdpm_dpsfid |  | fid |

---

## 促销类型校验配置-多语言表 t_ocdpm_promodeploy_l

- **表名称：** 促销类型校验配置-多语言表
- **表名：** t_ocdpm_promodeploy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 135 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_promodeployl_flid |  | fid,flocaleid |
| 2 | pk_ocdpm_promodeploy_l |  | fpkid |

---

## 促销类型校验配置-主表 t_ocdpm_promodeploy

- **表名称：** 促销类型校验配置-主表
- **表名：** t_ocdpm_promodeploy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 4 | fpromobjectid | 促销类别 | int8 | 64 |  | √ | 0 | [渠道促销类别 ocdpm_promotionobject](../ocdpm_files/ocdpm_promotionobject.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fladdertype | 阶梯类型 | bpchar | 1 |  | √ | 'A' | 阶梯类型,枚举: A :阶梯(最高阶梯计算) B :阶梯（每段均计算） C :无 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fpromrequire | 促销条件 | bpchar | 1 |  | √ | 'A' | 促销条件,枚举: A :按数量 B :按金额 C :按累计数量 D :按累计金额 |
| 13 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_promodeploy_num |  | fnumber |
| 2 | pk_ocdpm_promodeploy |  | fid |

---

## 促销策略【作废】-多选基础资料表 t_ocdpm_deploystrategy

- **表名称：** 促销策略【作废】-多选基础资料表
- **表名：** t_ocdpm_deploystrategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [渠道促销策略 ocdpm_promotionstrategy](../ocdpm_files/ocdpm_promotionstrategy.md) |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_deploystrategy |  | fpkid |
| 2 | idx_ocdpm_deploystr_fidbdid |  | fid,fbasedataid |
