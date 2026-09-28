# 行业要求映射-iq_industry_requirements

## 行业要求映射-主表 t_iq_industry_requirement

- **表名称：** 行业要求映射-主表
- **表名：** t_iq_industry_requirement

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdescribe | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 3 | fsort | 排序 | varchar | 50 |  | √ | ' ' | 排序 |
| 4 | fistraden | fistraden | bpchar | 1 |  | √ | '0' |  |
| 5 | furl | 跳转行业信息 | varchar | 200 |  | √ | ' ' | 跳转行业信息 |
| 6 | ftradenature | 行业属性 | varchar | 50 |  | √ | ' ' | 行业属性,枚举: 0 :鼓励行业 1 :限制行业 2 :禁止行业 |
| 7 | fquotainfo | 原子指标 | int8 | 64 |  | √ | 0 | [指标库 ipo_quota_info](../ipobase_files/ipo_quota_info.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_industry_requirement_quota |  | fquotainfo |
| 2 | pk_iq_industry_requirement |  | fid |

---

## 所属行业-多选基础资料表 t_iq_ir_placetraden

- **表名称：** 所属行业-多选基础资料表
- **表名：** t_iq_ir_placetraden

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [证监会行业 csrc_industry_info](../ipobase_files/csrc_industry_info.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iq_ir_placetraden |  | fpkid |
| 2 | idx_ir_placetraden_0 |  | fid |
