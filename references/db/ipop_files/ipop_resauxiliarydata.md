# 资源辅助资料-ipop_resauxiliarydata

## 资源辅助资料-多语言表 t_ipop_resauxiliarydata_l

- **表名称：** 资源辅助资料-多语言表
- **表名：** t_ipop_resauxiliarydata_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | '0' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ipop_resauxiliarydata_l |  | fpkid |
| 2 | idx_ipop_resauxiliarydata_l_id |  | fid |

---

## 资源辅助资料-主表 t_ipop_resauxiliarydata

- **表名称：** 资源辅助资料-主表
- **表名：** t_ipop_resauxiliarydata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fclassification | 分类 | varchar | 50 |  | √ | ' ' | 分类,枚举: productSeries :产品系列 moduleClassification :资源分类 moduleUnit :资源单位 |
| 4 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ipop_resauxiliarydata |  | fid |
| 2 | idx_ipop_resauxiliarydata_classification |  | fclassification |
