# 即征即退产品-tcvat_jzjt_product

## 即征即退产品-主表 t_tcvat_jzjt_product

- **表名称：** 即征即退产品-主表
- **表名：** t_tcvat_jzjt_product

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | 产品名称 | varchar | 150 |  | √ | ' ' | 产品名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fproductclassify | 产品分类 | varchar | 50 |  | √ | ' ' | 产品分类,枚举: jsjfj :计算机软件 xxxt :信息系统 qrsrj :嵌入式软件 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbizdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | ftaxplan | 计税方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 10 | fresourceuse | 综合利用的资源名称 | int8 | 64 |  | √ | 0 | 资源综合利用优惠目录分录 tpo_tcvat_resource_use_en |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fenddate | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 14 | fjzjtproject | 即征即退项目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcvat_bizdef_entity |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 17 | fstartdate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 18 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 产品编码 | varchar | 50 |  | √ | ' ' | 产品编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_jzjt_product |  | fid |
| 2 | idx_tcvatjzjtproduc_orgdatenum |  | forgid,fstartdate,fenddate,fnumber |

---

## 即征即退产品-多语言表 t_tcvat_jzjt_product_l

- **表名称：** 即征即退产品-多语言表
- **表名：** t_tcvat_jzjt_product_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 产品名称 | varchar | 50 |  | √ | ' ' | 产品名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_jzjt_product_l |  | fpkid |
| 2 | idx_tcvat_jzjt_product_l_0 |  | fid,flocaleid |
