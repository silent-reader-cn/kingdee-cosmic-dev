# 配置规则-pdm_chararule

## 配置规则-多语言表 t_pdm_chararule_l

- **表名称：** 配置规则-多语言表
- **表名：** t_pdm_chararule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 特征规则名称 | varchar | 50 |  | √ | ' ' | 特征规则名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_chararule_l |  | fpkid |
| 2 | idx_pdm_charlel_fid |  | fid,flocaleid |
| 3 | idx_pdm_charlel_fname |  | fname |

---

## 配置规则-主表 t_pdm_chararule

- **表名称：** 配置规则-主表
- **表名：** t_pdm_chararule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fclassify | 特征规则分类 | varchar | 5 |  | √ | 'A' | 特征规则分类,枚举: A :全局 B :局部 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fdisableuserid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fformulaalias | 中文公式 | varchar | 2000 |  | √ | ' ' | 中文公式 |
| 7 | fenabledate | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 8 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | ftype | 特征规则类型 | varchar | 5 |  | √ | '1' | 特征规则类型,枚举: 1 :前提 2 :选择 3 :公式 4 :约束 |
| 15 | fformula | 公式脚本 | varchar | 2000 |  | √ | ' ' | 公式脚本 |
| 16 | fenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fenableuserid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fnumber | 特征规则编码 | varchar | 30 |  | √ | ' ' | 特征规则编码 |
| 19 | frulegroupid | 特征规则组 | int8 | 64 |  | √ | 0 | [特征规则分组 pdm_chararulegrp](../pdm_files/pdm_chararulegrp.md) |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_chararule |  | fid |
| 2 | idx_pdm_charle_fnumber |  | fnumber |
| 3 | idx_pdm_charle_fcreatetime |  | fcreatetime |
