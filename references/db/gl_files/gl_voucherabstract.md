# 凭证摘要-gl_voucherabstract

## 凭证摘要-多语言表 t_gl_voucherabstract_l

- **表名称：** 凭证摘要-多语言表
- **表名：** t_gl_voucherabstract_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fabstract | 摘要内容 | varchar | 255 |  |  | ' ' | 摘要内容 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_voucherabstract_l_pkey |  | fpkid |
| 2 | idx_gl_vouvherabstract_l |  | fid,flocaleid |

---

## 凭证摘要-主表 t_gl_voucherabstract

- **表名称：** 凭证摘要-主表
- **表名：** t_gl_voucherabstract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 核算主体 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fabstract | 摘要内容 | varchar | 255 |  |  | ' ' | 摘要内容 |
| 8 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_voucherabstract_pkey |  | fid |
| 2 | idx_gl_voucherabstract |  | forgid |
